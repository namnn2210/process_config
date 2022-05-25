IMPS_CONFIG = [
    {
        "process": {
            "select": [
                "ad_id",
                "tag_id",
                "number",
                "price",
                "value_adv",
                "run_type"
            ],
            "group_by": [
                "ad_id",
                "tag_id"
            ],
            "agg": {
                "sum": [
                    {
                        "field": [
                            "price"
                        ],
                        "alias": "spent_cpm"
                    },
                    {
                        "field": [
                            "number"
                        ],
                        "alias": "imp"
                    }
                ]
            }
        },
        "table_name": "stats_ads_tags_date"
    }
]
