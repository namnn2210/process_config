REQUESTS_CONFIG = [
    {
        "process": {
            "select": [
                "tag_id",
                "request",
                "paid"
            ],
            "group_by": [
                "tag_id"
            ],
            "agg": {
                "sum": [
                    {
                        "field": [
                            "request"
                        ],
                        "alias": "request"
                    },
                    {
                        "field": [
                            "paid"
                        ],
                        "alias": "paid"
                    }
                ]
            }
        },
        "table_name": "stats_tags_date"
    },
    {
        "process": {
            "select": [
                "tag_id",
                "location1",
                "request",
                "paid"
            ],
            "group_by": [
                "tag_id",
                "location1"
            ],
            "agg": {
                "sum": [
                    {
                        "field": [
                            "request"
                        ],
                        "alias": "request"
                    },
                    {
                        "field": [
                            "paid"
                        ],
                        "alias": "paid"
                    }
                ]
            }
        },
        "table_name": "stats_tags_location"
    },
    {
        "process": {
            "select": [
                "tag_id",
                "device1",
                "device2",
                "request",
                "paid"
            ],
            "group_by": [
                "tag_id",
                "device1",
                "device2"
            ],
            "agg": {
                "sum": [
                    {
                        "field": [
                            "request"
                        ],
                        "alias": "request"
                    },
                    {
                        "field": [
                            "paid"
                        ],
                        "alias": "paid"
                    }
                ]
            }
        },
        "table_name": "stats_tags_device"
    },
    {
        "process": {
            "select": [
                "tag_id",
                "browser",
                "request",
                "paid"
            ],
            "group_by": [
                "tag_id",
                "browser"
            ],
            "agg": {
                "sum": [
                    {
                        "field": [
                            "request"
                        ],
                        "alias": "request"
                    },
                    {
                        "field": [
                            "paid"
                        ],
                        "alias": "paid"
                    }
                ]
            }
        },
        "table_name": "stats_tags_browser"
    },
    {
        "process": {
            "select": [
                "tag_id",
                "location1",
                "device1",
                "device2",
                "request",
                "paid"
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
                            "request"
                        ],
                        "alias": "request"
                    },
                    {
                        "field": [
                            "paid"
                        ],
                        "alias": "paid"
                    }
                ]
            }
        },
        "table_name": "stats_tags_inventories"
    }
]
