CAMPAIGN_CONFIG = [
    {
        "process": {
            "select": [
                "kmap",
                "tag_id",
                "campaign_id",
                "number",
                "price"
            ],
            "group_by": [
                "tag_id",
                "campaign_id",
                "kmap"
            ],
            "agg": {
                "sum": [
                    {
                        "field": [
                            "number"
                        ],
                        "alias": "imps"
                    },
                    {
                        "field": [
                            "price"
                        ],
                        "alias": "prices"
                    }
                ]
            }
        },
        "table_name": "stats_ads_tags_campaign_by_node_hour"
    },
    {
        "process": {
            "select": [
                "tag_id",
                "campaign_id",
                "imps",
                "kmap",
                "prices"
            ],
            "group_by": [
                "tag_id",
                "campaign_id"
            ],
            "agg": {
                "sum": [
                    {
                        "field": [
                            "imps"
                        ],
                        "alias": "imp"
                    },
                    {
                        "field": [
                            "prices"
                        ],
                        "alias": "spent_cpm"
                    }
                ],
                "count":[
                    {
                        "field": [
                            "kmap"
                        ],
                        "alias": "paid"
                    }
                ]
            }
        },
        "table_name": "stats_ads_tags_campaign_by_node_hour"
    }
]
