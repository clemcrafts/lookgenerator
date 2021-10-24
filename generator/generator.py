from scipy.stats import beta
from operator import itemgetter
from . import REWARD, BETA_SHAPE_PARAMETER_A, BETA_SHAPE_PARAMETER_B, COLD_START_LOOKS


class Generator:
    """
    MAB outfit generator learning online.
    i.e: POC based on pre-generated looks created by a human (cold start) to
    have a starting point for the algorithm to learn in realtime from there.
    """
    def __init__(self):
        """
        We simply keep all affinity profiles in memory for now.
        """
        self.profiles = {}
        self._init_arms()

    def generate(self, event):
        """
        Generates outfit based on reward for a combination (e.g: purchase).
        :param dict event: a reward event on a given articles combination.
        {"articles":
          [{"look": "cosy", "category": "slippers", "articleId": "11223344"},
           {"look": "cosy, "category": "trousers", "articleId": "55667788"},
           {"look": "cosy,, category": "tops", "articleId": "987654321"}}
        """
        self._update_arms(event)
        return self._generate_outfit()

    def _init_arms(self):
        """
        Initialise all levels of arms based on config.
        """
        for look, articles in COLD_START_LOOKS.items():
            self._init_look_arm(look)
            self._init_articles_arms(look, articles)

    def _init_article_arm(self, category, article, look):
        """
        Initialise one "article arm" based on config
        :param category: category for the arm.
        :param article: the article for the arm.
        :param look: the look of the arm.
        """
        if category not in self.profiles[look].keys():
            self.profiles[look][category] = {article["articleId"]: {
                    "distribution": [
                        BETA_SHAPE_PARAMETER_A,
                        BETA_SHAPE_PARAMETER_B],
                    "url": article["url"]}}
            return
        self.profiles[look][category][
            article["articleId"]] = {
            "distribution": [BETA_SHAPE_PARAMETER_A,
                             BETA_SHAPE_PARAMETER_B],
            "url": article["url"]}

    def _init_look_arm(self, look):
        """
        Initialise a "look level arm" based on config.
        """
        self.profiles[look] = {"distribution": [BETA_SHAPE_PARAMETER_A,
                                                BETA_SHAPE_PARAMETER_B]}

    def _init_articles_arms(self, look, articles):
        """
        Initialise all "article arms" based on config.
        """
        for category, articles in articles.items():
            for article in articles:
                self._init_article_arm(category, article, look)

    def _update_arms(self, event):
        """
        Updating all levels of arms using a Bayesian approach.
        :param dict event: a reward event.
        """
        self._update_look_arm(event)
        for article in event["articles"]:
            self._update_article_arm(article)

    def _update_look_arm(self, event):
        """
        Updating looks arm based on default reward defined in config.
        """
        self.profiles[event["articles"][0][
            "look"]]["distribution"][0] += REWARD
        self.profiles[event["articles"][0][
            "look"]]["distribution"][1] += 1 - REWARD

    def _update_article_arm(self, article):
        """
        Updating "article level arm" based on config..
        """
        self.profiles[article["look"]][
                      article["category"]][
                      article["articleId"]]["distribution"][0] += REWARD
        self.profiles[article["look"]][
                      article["category"]][
                      article["articleId"]]["distribution"][1] += (1-REWARD)

    def _thompson_sample_outfits(self, looks_profiles):
        """
        Thompson sample outfits.
        :param list looks_profiles: looks profiles..
        :return dict winning_look: the look picked by the Thomson Sampling.
        """
        for name, look in self.profiles.items():
            looks_profiles.append(
                {"reward": beta.rvs(
                    look["distribution"][0], look["distribution"][1]),
                    "name": name})
        looks_profiles.sort(key=itemgetter('reward'), reverse=True)
        winning_look = looks_profiles[0]
        return winning_look


    def _thompson_sample_articles(self, winning_look, looks_profiles):
        """
        Thompson sample articles within categories for the outfit.
        n.b: It does more than what it says, to simplify.
        :param winning_look: the winning look to fill with articles.
        :param list looks_profiles: looks profiles..
        :return dict winning_look: the look with articles selected by TS.
        """
        winning_look_name = looks_profiles[0]["name"]
        items = self.profiles[winning_look_name]
        articles_profiles = {}
        for category, articles in items.items():
            if category == "distribution":
                continue
            articles_profiles[category] = []
            for article_id, article_values in articles.items():
                articles_profiles[category].append((article_id, beta.rvs(
                    article_values["distribution"][0],
                    article_values["distribution"][1]),
                                                    article_values["url"] ))
        for category, distributions in articles_profiles.items():
            winning_article = sorted(
                distributions, key=itemgetter(1), reverse=True)[0]
            winning_look[category] = {'articleId': winning_article[0],
                                      "reward": winning_article[1],
                                      "url": winning_article[2]}
        return winning_look

    def _generate_outfit(self):
        """
        Generate top outfit by drawing an arm with top article by category.
        """
        looks_profiles = []
        look = self._thompson_sample_outfits(looks_profiles)
        look = self._thompson_sample_articles(look, looks_profiles)
        return look
