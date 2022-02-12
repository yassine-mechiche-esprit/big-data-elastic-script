ELASTIC_MAPPING_SETTINGS = {
	"aliases": { },
    "settings": {
		"analysis": {
			"analyzer": {
				"facebook": {
					"type": "custom",
					"tokenizer": "standard",
					"filter": [
						"lowercase",
						"asciifolding",
					]
				}
			},
			"normalizer": {
				"facebook_normalizer": {
					"type": "custom",
					"filter": [
						"lowercase", 
						"asciifolding"
					]
				}
			},
			"filter": {
				"shingle": {
					"type": "shingle"
				}
			}
		},
		"max_result_window": 100000
	}
}

ELASTIC_MAPPING = {
	"properties": {
		"facebook": {
			"properties": {
				'userid': {
					'type': 'text',
					'analyzer': 'facebook'
				},
				'age': {
					'type': 'text',
					'analyzer': 'facebook'
				},
				'dob_day': {
					'type': 'text',
					'analyzer': 'facebook'
				},
				'dob_year': {
					'type': 'text',
					'analyzer': 'facebook'
				},
				'dob_month': {
					'type': 'text',
					'analyzer': 'facebook'
				},
				'gender': {
					'type': 'text',
					'analyzer': 'facebook'
				},
				'tenure': {
					'type': 'text',
					'analyzer': 'facebook'
				},
				'friend_count': {
					'type': 'text',
					'analyzer': 'facebook'
				},
				'friendships_initiated': {
					'type': 'text',
					'analyzer': 'facebook'
				},
				'likes': {
					'type': 'text',
					'analyzer': 'facebook'
				},
				'likes_received': {
					'type': 'text',
					'analyzer': 'facebook'
				},
				'mobile_likes': {
					'type': 'text',
					'analyzer': 'facebook'
				},
				'mobile_likes_received': {
					'type': 'text',
					'analyzer': 'facebook'
				},
				'www_likes': {
					'type': 'text',
					'analyzer': 'facebook'
				},
				'www_likes_received': {
					'type': 'text',
					'analyzer': 'facebook'
				}
			},
		},
	}
}