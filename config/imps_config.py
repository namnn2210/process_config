IMPS_CONFIG = [
    {
        "nested": False,
        "process": {
            "select": [
                "ad_id",
                "tag_id",
                "number",
                "price"
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
        "table_name": "stats_ads_tags_dat_by_node_hour"
    },
    {
        "nested": False,
        "process": {
            "select": [
                "ad_id",
                "tag_id",
                "number",
                "price",
                "location1"
            ],
            "group_by": [
                "ad_id",
                "tag_id",
                "location1"
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
        "table_name": "stats_ads_tags_location_by_node_hour"
    },
    {
        "nested": False,
        "process": {
            "select": [
                "ad_id",
                "tag_id",
                "device1",
                "device2",
                "number",
                "price",
            ],
            "group_by": [
                "ad_id",
                "tag_id",
                "device1",
                "device2"
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
        "table_name": "stats_ads_tags_device_by_node_hour"
    },
    {
        "nested": False,
        "process": {
            "select": [
                "ad_id",
                "tag_id",
                "browser",
                "number",
                "price",
            ],
            "group_by": [
                "ad_id",
                "tag_id",
                "browser"
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
        "table_name": "stats_ads_tags_browser_by_node_hour"
    },
    {
        "nested": False,
        "process": {
            "select": [
                "tag_id",
                "location1",
                "device1",
                "device2",
                "number",
                "price",
                "run_type",
                "value_adv"
            ],
            "group_by": [
                "tag_id",
                "location1",
                "device1",
                "device2"
            ],
            "agg": {
                "sum": [
                    {
                        "field": [
                            "price",
                            "run_type",
                            "value_adv"
                        ],
                        "alias": "spent_cpm",
                        "group": "multiple"
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
        "table_name": "stats_tags_inventories_by_node_hour"
    },
    {
        "nested": False,
        "process": {
            "select": [
                "ad_id",
                "tag_id",
                "location1",
                "device1",
                "device2",
                "number",
                "price",
                "run_type",
                "value_adv"
            ],
            "group_by": [
                "ad_id",
                "tag_id",
                "location1",
                "device1",
                "device2"
            ],
            "agg": {
                "sum": [
                    {
                        "field": [
                            "price",
                            "run_type",
                            "value_adv"
                        ],
                        "alias": "spent_cpm",
                        "group": "multiple"
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
        "table_name": "stats_ads_performance_by_node_hour"
    },
    {
        "nested": True,
        "process_1": {
            "select": [
                "kmap",
                "tag_id",
                "campaign_id",
                "number",
                "price"
            ],
            "group_by": [
                "kmap",
                "tag_id",
                "campaign_id"
            ],
            "agg": {
                "sum": [
                    {
                        "field": [
                            "number",
                        ],
                        "alias": "imps",
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
        "process_2": {
            "select": [
                "kmap",
                "tag_id",
                "campaign_id",
                "number",
                "price"
            ],
            "group_by": [
                "kmap",
                "tag_id",
                "campaign_id"
            ],
            "agg": {
                "sum": [
                    {
                        "field": [
                            "number",
                        ],
                        "alias": "imps",
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
    }
]
