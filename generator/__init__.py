import os

BETA_SHAPE_PARAMETER_A = 2.0
BETA_SHAPE_PARAMETER_B = 2.0
REWARD = 0.7

COLD_START_LOOKS = {
            "cosy": {"shoes": [
                           {"articleId": "60507697", "url": "https://asset1.cxnmarksandspencer.com/is/image/mands/Felt-Pom-Pom-Faux-Fur-Mule-Slippers-2/SD_01_T02_3306S_T1_X_EC_90"},
                           {"articleId": "60516866", "url": "https://asset1.cxnmarksandspencer.com/is/image/mands/Checked-Faux-Fur-Slipper-Boots-2/SD_01_T02_3882A_B4_X_EC_1"},
                           {"articleId": "60504718", "url": "https://asset1.cxnmarksandspencer.com/is/image/mands/Felt-Slipper-Boots-with-Secret-Support-2/SD_01_T02_3899_T3_X_EC_1"}],
                     "trousers": [
                           {"articleId": "60517412", "url": "https://asset1.cxnmarksandspencer.com/is/image/mands/Velour-Tapered-Ankle-Grazer-Joggers-1/SD_01_T57_7155_F0_X_EC_90"},
                           {"articleId": "60496582", "url": "https://asset1.cxnmarksandspencer.com/is/image/mands/Animal-Print-High-Waisted-Leggings-2/SD_01_T57_9791_N4_X_EC_90"},
                           {"articleId": "60485553", "url": "https://asset1.cxnmarksandspencer.com/is/image/mands/Go-Move-7-8-Gym-Leggings-2/SD_01_T51_6295_UT_X_EC_90"}],
                     "tops": [
                           {"articleId": "60520753", "url": "https://asset1.cxnmarksandspencer.com/is/image/mands/Pure-Cotton-High-Neck-Sweatshirt-2/SD_01_T41_6296C_ND_X_EC_90"},
                           {"articleId": "60505009", "url": "https://asset1.cxnmarksandspencer.com/is/image/mands/Pure-Cotton-Striped-Straight-Fit-Top-2/SD_01_T41_4687_F4_X_EC_90"},
                           {"articleId": "60513683", "url": "https://asset1.cxnmarksandspencer.com/is/image/mands/Cotton-Ribbed-V-Neck-Longline-Top-2/SD_01_T41_6284C_VP_X_EC_90"}]},
            "hipster": {"shoes": [
                           {"articleId": "60478094", "url": "https://asset1.cxnmarksandspencer.com/is/image/mands/Wide-Fit-Leather-Chelsea-Ankle-Boots-2/SD_01_T02_6385W_VS_X_EC_90"},
                           {"articleId": "60505645", "url": "https://asset1.cxnmarksandspencer.com/is/image/mands/The-Chunky-Chelsea-Boots-2/SD_01_T02_5989_SU_X_EC_90"},
                           {"articleId": "60505721", "url": "https://asset1.cxnmarksandspencer.com/is/image/mands/Wide-Fit-Leather-Lace-Up-Flat-Ankle-Boots-2/SD_01_T02_6388W_Y0_X_EC_1"}],
                       "trousers": [
                           {"articleId": "60519768", "url": "https://asset1.cxnmarksandspencer.com/is/image/mands/Jersey-Flared-Trousers-2/SD_01_T59_1203T_Y0_X_EC_90"},
                           {"articleId": "60539078", "url": "https://asset1.cxnmarksandspencer.com/is/image/mands/Leather-Wide-Leg-Culottes-2/SD_10_T97_7336B_JR_X_EC_90"},
                           {"articleId": "60517410", "url": "https://asset1.cxnmarksandspencer.com/is/image/mands/Side-Stripe-Wide-Leg-Trousers-2/SD_01_T57_7671_Y0_X_EC_90"}],
                       "tops": [
                           {"articleId": "60536077", "url": "https://asset1.cxnmarksandspencer.com/is/image/mands/Polka-Dot-Round-Neck-Puff-Sleeve-Top-1/SD_01_T43_4851_Y4_X_EC_90?"},
                           {"articleId": "60533820", "url": "https://asset1.cxnmarksandspencer.com/is/image/mands/Maternity-Tencel--Denim-Relaxed-Shirt-1/SD_01_T41_5500W_HP_X_EC_90?"},
                           {"articleId": "60507692", "url": "https://asset1.cxnmarksandspencer.com/is/image/mands/The-Tencel--Denim-Frill-Detail-Blouse-2/SD_01_T41_5024W_HP_X_EC_90"}]},
            "formal": {"shoes": [
                           {"articleId": "60168873", "url": "https://asset1.cxnmarksandspencer.com/is/image/mands/Wide-Fit-Block-Heel-Court-Shoes-2/SD_01_T02_1292W_F0_X_EC_90"},
                           {"articleId": "60464308", "url": "https://asset1.cxnmarksandspencer.com/is/image/mands/Stiletto-Heel-Pointed-Court-Shoes-2/SD_01_T02_2289A_Y0_X_EC_90"},
                           {"articleId": "22471001", "url": "https://asset1.cxnmarksandspencer.com/is/image/mands/Patent-Stiletto-Heel-Court-Shoes-2/SD_01_T02_0640_Y1_X_EC_90"}],
                      "trousers": [
                           {"articleId": "22531116", "url": "https://asset1.cxnmarksandspencer.com/is/image/mands/Elasticated-Waist-Wide-Leg-Trousers-2/SD_10_T83_3653_Y0_X_EC_90"},
                           {"articleId": "60506842", "url": "https://asset1.cxnmarksandspencer.com/is/image/mands/Jersey-Houndstooth-Straight-Leg-Trousers-2/SD_01_T59_7590_PK_X_EC_90"},
                           {"articleId": "60514482", "url": "https://asset1.cxnmarksandspencer.com/is/image/mands/Ponte-Slim-Fit-Cigarette-Trousers-3/SD_08_T97_7317A_F0_X_EC_1"}],
                      "tops": [
                           {"articleId": "60476826", "url": "https://asset1.cxnmarksandspencer.com/is/image/mands/Heatgen-Plus--Fleece-Thermal-Top-2/SD_02_T32_9210_Y0_X_EC_90"},
                           {"articleId": "60525148", "url": "https://asset1.cxnmarksandspencer.com/is/image/mands/Scoop-Neck-Long-Sleeve-Top-2/SD_01_T43_7803_Y0_X_EC_90"},
                           {"articleId": "60459094", "url": "https://asset1.cxnmarksandspencer.com/is/image/mands/Cotton-Funnel-Neck-Fitted-Long-Sleeve-Top-2/SD_01_T41_8770_Y0_X_EC_90"}]
                           }}
