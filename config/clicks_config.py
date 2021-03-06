CLICKS_CONFIG = [
    {
        "process": {
            "select": [
                "ad_id",
                "tag_id",
                "number",
                "price_click"
            ],
            "group_by": [
                "ad_id",
                "tag_id"
            ],
            "agg": {
                "sum": [
                    {
                        "field": [
                            "price_click"
                        ],
                        "alias": "spent_cpc_raw"
                    },
                    {
                        "field": [
                            "number"
                        ],
                        "alias": "click_raw"
                    }
                ]
            }
        },
        "table_name": "stats_ads_tags_date_by_node_hour"
    },
    {
        "process": {
            "select": [
                "ad_id",
                "tag_id",
                "number",
                "price_click",
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
                            "price_click"
                        ],
                        "alias": "spent_cpc_raw"
                    },
                    {
                        "field": [
                            "number"
                        ],
                        "alias": "click_raw"
                    }
                ]
            }
        },
        "table_name": "stats_ads_tags_location_by_node_hour"
    },
    {
        "process": {
            "select": [
                "ad_id",
                "tag_id",
                "device1",
                "device2",
                "number",
                "price_click",
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
                            "price_click"
                        ],
                        "alias": "spent_cpc_raw"
                    },
                    {
                        "field": [
                            "number"
                        ],
                        "alias": "click_raw"
                    }
                ]
            }
        },
        "table_name": "stats_ads_tags_device_by_node_hour"
    },
    {
        "process": {
            "select": [
                "ad_id",
                "tag_id",
                "browser",
                "number",
                "price_click",
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
                            "price_click"
                        ],
                        "alias": "spent_cpc_raw"
                    },
                    {
                        "field": [
                            "number"
                        ],
                        "alias": "click_raw"
                    }
                ]
            }
        },
        "table_name": "stats_ads_tags_browser_by_node_hour"
    },
    {
        "process": {
            "select": [
                "tag_id",
                "location1",
                "device1",
                "device2",
                "number",
                "price_click",
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
                            "price_click",
                            "run_type",
                            "value_adv"
                        ],
                        "alias": "spent_cpc_raw",
                        "group": "multiple"
                    },
                    {
                        "field": [
                            "number"
                        ],
                        "alias": "click_raw"
                    }
                ]
            }
        },
        "table_name": "stats_tags_inventories_by_node_hour"
    },
    {
        "process": {
            "select": [
                "ad_id",
                "tag_id",
                "location1",
                "device1",
                "device2",
                "number",
                "price_click",
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
                            "price_click",
                            "run_type",
                            "value_adv"
                        ],
                        "alias": "spent_cpc_raw",
                        "group": "multiple"
                    },
                    {
                        "field": [
                            "number"
                        ],
                        "alias": "click_raw"
                    }
                ]
            }
        },
        "table_name": "stats_ads_performance_by_node_hour"
    },
    {
        "process": {
            "select": [
                "tag_id",
                "campaign_id",
                "number",
                "price_click"
            ],
            "group_by": [
                "tag_id",
                "campaign_id"
            ],
            "agg": {
                "sum": [
                    {
                        "field": [
                            "number"
                        ],
                        "alias": "click_raw"
                    },
                    {
                        "field": [
                            "price_click"
                        ],
                        "alias": "spent_cpc_raw"
                    }
                ]
            }
        },
        "table_name": "stats_ads_tags_campaign_by_node_hour"
    }
]
