# Beryl_profile_longcong
Beryl Consulting data scientist project


# Clone repositories

```
git clone 'https://github.com/RicoXu727/Beryl_profile_longcong.git'
```

Install required packages
```
pip install -r requirements.txt
```

# First : Connect to Twitter database via API

Example of one scraped data record
```
{"created_at": "Tue Jan 10 17:38:33 +0000 2023", 
"id": 1612866496920981504, 
"id_str": "1612866496920981504", 
"full_text": "Intel Capital's Managing Director &amp; Head of Investment Operations @jenny_ard sits on the board of directors for Fabric8Labs &amp; is proud to work with the team to support their unique printing process that disrupts traditional high-precision metal manufacturing methods.", "truncated": false, "display_text_range": [0, 275], 
"entities": {"hashtags": [], "symbols": [], "user_mentions": [{"screen_name": "jenny_ard", "name": "Jennifer Ard", "id": 4073475314, "id_str": "4073475314", "indices": [70, 80]}], "urls": []}, "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>", "in_reply_to_status_id": 1612866495536836609, "in_reply_to_status_id_str": "1612866495536836609", "in_reply_to_user_id": 27994823, "in_reply_to_user_id_str": "27994823", "in_reply_to_screen_name": "intelcapital", "user": {"id": 27994823, "id_str": "27994823", "name": "Intel Capital", "screen_name": "intelcapital", "location": "Santa Clara, CA", "description": "A force multiplier for early stage startups - inspiring and investing in the future of compute.", "url": "https://t.co/RmwMrNPuPq", "entities": {"url": {"urls": [{"url": "https://t.co/RmwMrNPuPq", "expanded_url": "http://www.intelcapital.com", "display_url": "intelcapital.com", "indices": [0, 23]}]}, "description": {"urls": []}}, "protected": false, "followers_count": 29130, "friends_count": 1102, "listed_count": 1130, "created_at": "Tue Mar 31 23:33:16 +0000 2009", "favourites_count": 1758, "utc_offset": null, "time_zone": null, "geo_enabled": true, "verified": true, "statuses_count": 5828, "lang": null, "contributors_enabled": false, "is_translator": false, "is_translation_enabled": false, "profile_background_color": "028CD7", "profile_background_image_url": "http://abs.twimg.com/images/themes/theme4/bg.gif", "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme4/bg.gif", "profile_background_tile": false, "profile_image_url": "http://pbs.twimg.com/profile_images/1468279253242314752/Afa7DCr7_normal.jpg", 
"profile_image_url_https": "https://pbs.twimg.com/profile_images/1468279253242314752/Afa7DCr7_normal.jpg", 
"profile_banner_url": "https://pbs.twimg.com/profile_banners/27994823/1638900028", "profile_link_color": "0099B9", "profile_sidebar_border_color": "FFFFFF", "profile_sidebar_fill_color": "F2F2F2", "profile_text_color": "000000", "profile_use_background_image": true, "has_extended_profile": false, "default_profile": false, "default_profile_image": false, "following": false, "follow_request_sent": false, 
"notifications": false, "translator_type": "none", "withheld_in_countries": []}, "geo": null, 
"coordinates": null, "place": null, "contributors": null, "is_quote_status": false, 
"retweet_count": 0, "favorite_count": 0, "favorited": false, "retweeted": false, "lang": "en"}
```


# Second : deal with raw data

After getting the data, by getting all the keys in the json, I filtered out some attributes that I thought were useful for the study and directly removed some redundant variables. Then write to csv file line by line.

To evaluate the quality of the data, I use BART (Bidirectional and Auto-Regressive Transformers) language model which is a denoising self-encoder designed for pre-training sequence-to-sequence models proposed by Facebook. This model can find typos, jumbled characters and correct them. I compare the sentences output by the model with the original text and use ROUGE (Recall-Oriented Understudy for Gisting Evaluation) to calculate the deviation between them. If the deviation is large, it means that the original text has low quality data, and if the deviation is small, it means that the data found from Twitter is of high quality.

Transform the data into a pandas format that is suitable for data mining. 

# Correlate and cluster their engagements with other professional peers and/or companies.



# Collect and monitor the content they share

Use the poll function to update the collected data each time a request is sent

# Identify potential areas of interest or collaboration based on the data collected. 

Determine their investment type and investment direction


# References

Topic modeling(LDA): 

```
https://towardsdatascience.com/end-to-end-topic-modeling-in-python-latent-dirichlet-allocation-lda-35ce4ed6b3e0
```

Named-Entity-Recognition (NER) on Twitter with Bi-directional LSTM with tensorflow in python : 

```
https://sandipanweb.wordpress.com/2020/08/30/named-entity-recognition-ner-on-twitter-with-bi-directional-lstm-with-tensorflow-in-python/
```