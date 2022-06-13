REPORT_CONFIG = [
    {
        'sql': """
SELECT t1.tag_id,
       t1.ad_id,
       t2.campaign_id AS camp_id,
       t1.date,
       IFNULL(t1.imp,0) AS imp,
       2 AS source_id,
       IFNULL(t1.click_raw,0) AS click_raw,
       IFNULL(t1.click_landing,0) AS click_landing,
       IFNULL(t1.click_raw,0) AS click,
       IFNULL(t1.spent_cpm,0) AS spent_cpm,
       IFNULL(t1.spent_cpc_raw,0) AS spent_cpc_raw,
       IFNULL(t1.spent_cpc_landing,0) AS spent_cpc_landing,
       CASE tt2.target 
	   WHEN  2 THEN spent_cpc_raw
	   ELSE IFNULL(t1.spent_cpm, 0) 
       END AS spent,	   
       IFNULL(t3.payout,0) AS rev_opt,
       CASE 
           WHEN tt2.bg_own=1 THEN IFNULL(t3.payout, 0)
           WHEN tt2.bg_own=0 AND tt2.target=2 THEN t1.spent_cpc_raw
           ELSE IFNULL(t1.spent_cpm, 0)
       END AS rev_real,
       IFNULL(t3.conversions,0) AS conversions
FROM
  (SELECT tag_id,
          ad_id, DATE, SUM(imp) AS imp,
                       SUM(click_raw) AS click_raw,
                       SUM(click_landing) AS click_landing,
                       SUM(spent_cpm) AS spent_cpm,
                       SUM(spent_cpc_raw) AS spent_cpc_raw,
                       SUM(spent_cpc_landing) AS spent_cpc_landing
   FROM stats_ads_tags_date_by_node_hour
   WHERE DATE={date}

   GROUP BY tag_id, ad_id, DATE) t1
LEFT JOIN ads t2 ON t1.ad_id= t2.id
LEFT JOIN `campaigns` tt2 ON t2.campaign_id=tt2.id
LEFT JOIN
  (SELECT tag_id,
          ad_id,
          DATE,
          SUM(conversions) AS conversions,
          SUM(payout) AS payout
          
   FROM conversions_click
   WHERE DATE={date}
   GROUP BY tag_id, ad_id,DATE
	) t3 ON t1.tag_id=t3.tag_id
AND t1.ad_id=t3.ad_id
AND t1.date=t3.date;
    """,
        'index': ['tag_id', 'date', 'ad_id'],
        'table_name': 'stats_ads_tags_date_by_node_hour'
    },
    {
        'sql': """
SELECT tt1.tag_id,
       tt1.date,
       1 AS source_id,
       IFNULL(tt1.request, 0) AS request,
       IFNULL(tt1.paid, 0) AS paid,
       IFNULL(t1.imp, 0) AS imp,
       IFNULL(t1.click_raw, 0) AS click_raw,
       IFNULL(t1.click_landing, 0) AS click_landing,
       IFNULL(t1.click_raw, 0) AS click,
       IFNULL(t1.spent_cpm, 0) AS spent_cpm,
       IFNULL(t1.spent_cpc_raw, 0) AS spent_cpc_raw,
       IFNULL(t1.spent_cpc_landing, 0) AS spent_cpc_landing,
       IFNULL(t1.spent, 0) AS spent,
       IFNULL(t3.payout, 0) AS rev_opt,
       IFNULL(rev_real, 0) AS rev_real,
       IFNULL(tt1.ctr, 0) AS ctr
FROM
  (SELECT tag_id, DATE, SUM(request) AS request,
                        SUM(paid) AS paid,
                        SUM(ctr) AS ctr
   FROM bg_dsp4.stats_tags_date_by_node_hour
   WHERE DATE={date}
   GROUP BY tag_id,DATE) tt1
LEFT JOIN
  (SELECT tag_id, DATE, SUM(imp) AS imp,
                        SUM(click_raw) AS click_raw,
                        SUM(click_landing) AS click_landing,
                        SUM(spent_cpm) AS spent_cpm,
                        SUM(spent_cpc_raw) AS spent_cpc_raw,
                        SUM(spent_cpc_landing) AS spent_cpc_landing,
                        SUM(spent) AS spent,
                        SUM(rev_real) AS rev_real
   FROM stats_ads_tags_date
   WHERE DATE={date}
   GROUP BY tag_id, DATE) t1 ON tt1.tag_id = t1.tag_id
AND tt1.date = t1.date
LEFT JOIN
  (SELECT tag_id,
          SUM(payout) AS payout,
          SUM(conversions) AS conversions, 
          DATE
   FROM conversions_click
   WHERE DATE={date}
   GROUP BY tag_id) t3 ON tt1.tag_id=t3.tag_id AND tt1.date=t3.date;
    """,
        'index': ['tag_id', 'date'],
        'table_name': 'stats_tags_date_by_node_hour'
    },
    {
        'sql': """
SELECT t1.tag_id,
       t1.ad_id,
       t1.date,
       t1.device1,
       t1.device2,
       IFNULL(t1.imp, 0) AS imp,
       2 AS source_id,
       IFNULL(t1.click_raw, 0) AS click_raw,
       IFNULL(t1.click_landing, 0) AS click_landing,
       IFNULL(t1.click_raw, 0) AS click,
       IFNULL(t1.spent_cpm, 0) AS spent_cpm,
       IFNULL(t1.spent_cpc_raw, 0) AS spent_cpc_raw,
       IFNULL(t1.spent_cpc_landing, 0) AS spent_cpc_landing,
        CASE tt2.target 
	   WHEN  2 THEN spent_cpc_raw
	   ELSE IFNULL(t1.spent_cpm, 0) 
       END AS spent,
       IFNULL(t3.payout, 0) AS rev_opt,
            CASE 
           WHEN tt2.bg_own=1 THEN IFNULL(t3.payout, 0)
           WHEN tt2.bg_own=0 AND tt2.target=2 THEN t1.spent_cpc_raw
           ELSE IFNULL(t1.spent_cpm, 0)
       END AS rev_real
FROM
  (SELECT tag_id,
          ad_id,
                       device1,
                       device2,          
           DATE, SUM(imp) AS imp,
                       SUM(click_raw) AS click_raw,
                       SUM(click_landing) AS click_landing,
                       ROUND(SUM(spent_cpm)/1000,0) AS spent_cpm,
                       SUM(spent_cpc_raw) AS spent_cpc_raw,
                       SUM(spent_cpc_landing) AS spent_cpc_landing
   FROM stats_ads_tags_device_by_node_hour
   WHERE DATE={date}

   GROUP BY tag_id,
            ad_id,device1,device2, DATE) t1
LEFT JOIN ads t2 ON t1.ad_id= t2.id
LEFT JOIN `campaigns` tt2 ON t2.campaign_id=tt2.id
LEFT JOIN
  (SELECT tag_id,
          ad_id,
          device1,
          device2,
          SUM(payout) AS payout, DATE
   FROM conversions_click
   WHERE DATE={date}
   GROUP BY tag_id,
            ad_id,device1,device2) t3 ON t1.tag_id=t3.tag_id
AND t1.device1 = t3.device1
AND t1.device2 = t3.device2
AND t1.ad_id=t3.ad_id
AND t1.date=t3.date
    """,
        'index': ['tag_id', 'date', 'ad_id', 'device1', 'device2'],
        'table_name': 'stats_ads_tags_device_by_node_hour'
    },
    {
        'sql': """
SELECT 	tt1.tag_id, 
	tt1.date, 
	tt1.device1, 
	tt1.device2, 
	1 AS source_id, 
	IFNULL(tt1.request,0) AS request, 
	IFNULL(tt1.paid,0) AS paid, 
	IFNULL(t1.imp,0) AS imp, 
	IFNULL(t1.click_raw,0) AS click_raw, 
	IFNULL(t1.click_landing,0) AS click_landing, 
	IFNULL(t1.click_raw,0) AS click, 
	IFNULL(t1.spent_cpm,0) AS spent_cpm, 
	IFNULL(t1.spent_cpc_raw,0) AS spent_cpc_raw, 
	IFNULL(t1.spent_cpc_landing,0) AS spent_cpc_landing, 
	IFNULL(t1.spent,0) AS spent, 	
	IFNULL(t1.rev_opt,0) AS rev_opt, 
	IFNULL(t1.rev_real,0) AS rev_real
	 
FROM  (
SELECT tag_id, 
	device1,
	device2,
	DATE,
       SUM(request) AS request,
       SUM(paid) AS paid
   FROM stats_tags_device_by_node_hour 
   WHERE DATE={date}
   GROUP BY tag_id,device1, device2,DATE
)
 tt1 LEFT JOIN
(SELECT tag_id,
	device1,
	device2,
	SUM(imp) AS imp,
	SUM(click_raw) AS click_raw,
	SUM(click_landing) AS click_landing,
	SUM(spent_cpm) AS spent_cpm,
	SUM(spent_cpc_raw) AS spent_cpc_raw,
	SUM(spent_cpc_landing) AS spent_cpc_landing,
	SUM(spent) AS spent,
	SUM(rev_opt) AS rev_opt,
	SUM(rev_real) AS rev_real
FROM bg_dsp4.stats_ads_tags_device WHERE DATE={date}
   
GROUP BY tag_id,device1, device2)  t1 ON  tt1.tag_id = t1.tag_id AND tt1.device1 = t1.device1 AND tt1.device2 = t1.device2
    """,
        'index': ['tag_id', 'date', 'device1', 'device2'],
        'table_name': 'stats_tags_device_by_node_hour'
    },
    {
        'sql': """
SELECT t1.tag_id,
       t1.ad_id,
       t1.date,
       t1.location1,
       t1.location2,
       IFNULL(t1.imp,0) AS imp,
       2 AS source_id,
       IFNULL(t1.click_raw,0) AS click_raw,
       IFNULL(t1.click_landing,0) AS click_landing,
       IFNULL(t1.click_raw,0) AS click,
       IFNULL(t1.spent_cpm,0) AS spent_cpm,
       IFNULL(t1.spent_cpc_raw,0) AS spent_cpc_raw,
       IFNULL(t1.spent_cpc_landing,0) AS spent_cpc_landing,
       CASE tt2.target 
	   WHEN  2 THEN spent_cpc_raw
	   ELSE IFNULL(t1.spent_cpm, 0) 
       END AS spent,
	   
       IFNULL(t3.payout,0) AS rev_opt,
        CASE 
           WHEN tt2.bg_own=1 THEN IFNULL(t3.payout, 0)
           WHEN tt2.bg_own=0 AND tt2.target=2 THEN t1.spent_cpc_raw
           ELSE IFNULL(t1.spent_cpm, 0)
       END AS rev_real
FROM
  (SELECT tag_id,
          ad_id, 
			location1,
			location2,
			DATE, 
			SUM(imp) AS imp,
                       SUM(click_raw) AS click_raw,
                       SUM(click_landing) AS click_landing,
                       ROUND(SUM(spent_cpm)/1000,0) AS spent_cpm,
                       SUM(spent_cpc_raw) AS spent_cpc_raw,
                       SUM(spent_cpc_landing) AS spent_cpc_landing
   FROM stats_ads_tags_location_by_node_hour
   WHERE DATE={date}

   GROUP BY tag_id, ad_id,location1,location2, DATE) t1
LEFT JOIN ads t2 ON t1.ad_id= t2.id
LEFT JOIN `campaigns` tt2 ON t2.campaign_id=tt2.id
LEFT JOIN
  (SELECT tag_id,
          ad_id,
	  location1,
          SUM(payout) AS payout,
          DATE
   FROM conversions_click
   WHERE DATE={date}
   GROUP BY tag_id, ad_id, location1
	) t3 ON t1.tag_id=t3.tag_id 
AND t1.location1 = t3.location1
AND t1.ad_id=t3.ad_id
AND t1.date=t3.date
    """,
        'index': ['tag_id', 'date', 'ad_id', 'location1', 'location2'],
        'table_name': 'stats_ads_tags_location_by_node_hour'
    },
    {
        'sql': """
SELECT tt1.tag_id,
       tt1.date,
       tt1.location1,
       0 AS location2,
       1 AS source_id,
       IFNULL(tt1.request,0) AS request,
       IFNULL(tt1.paid,0) AS paid,
       IFNULL(t1.imp,0) AS imp,
       IFNULL(t1.click_raw,0) AS click_raw,
       IFNULL(t1.click_landing,0) AS click_landing,
       IFNULL(t1.click_raw,0) AS click,
       IFNULL(t1.spent_cpm,0) AS spent_cpm,
       IFNULL(t1.spent_cpc_raw,0) AS spent_cpc_raw,
       IFNULL(t1.spent_cpc_landing,0) AS spent_cpc_landing,
       IFNULL(t1.spent,0) AS spent,
       IFNULL(t1.rev_opt, 0) AS rev_opt,
       IFNULL(t1.rev_real, 0) AS rev_real
FROM
  (SELECT tag_id, location1,
			DATE,
                        SUM(request) AS request,
                        SUM(paid) AS paid
   FROM stats_tags_location_by_node_hour
   WHERE DATE={date}
   GROUP BY tag_id,
            location1,DATE) tt1
LEFT JOIN
  (SELECT tag_id,
          location1,
          SUM(imp) AS imp,
          SUM(click_raw) AS click_raw,
          SUM(click_landing) AS click_landing,
          SUM(spent_cpm) AS spent_cpm,
          SUM(spent_cpc_raw) AS spent_cpc_raw,
          SUM(spent_cpc_landing) AS spent_cpc_landing,
          SUM(spent) AS spent,
          SUM(rev_opt) AS rev_opt,
          SUM(rev_real) AS rev_real
   FROM bg_dsp4.stats_ads_tags_location
   WHERE DATE={date}
   GROUP BY tag_id,
            location1) t1 ON tt1.tag_id = t1.tag_id
AND tt1.location1 = t1.location1
    """,
        'index': ['tag_id', 'date', 'location1', 'location2'],
        'table_name': 'stats_tags_location_by_node_hour'
    },
    {
        'sql': """
SELECT t1.tag_id,
       t1.ad_id,
       t1.date,
       t1.browser,
       IFNULL(t1.imp,0) AS imp,
       2 AS source_id,
       IFNULL(t1.click_raw,0) AS click_raw,
       IFNULL(t1.click_landing,0) AS click_landing,
       IFNULL(t1.click_raw,0) AS click,
       IFNULL(t1.spent_cpm,0) AS spent_cpm,
       IFNULL(t1.spent_cpc_raw,0) AS spent_cpc_raw,
       IFNULL(t1.spent_cpc_landing,0) AS spent_cpc_landing,
       CASE tt2.target 
	   WHEN  2 THEN spent_cpc_raw
	   ELSE IFNULL(t1.spent_cpm, 0) 
       END AS spent,
	   
       IFNULL(t3.payout,0) AS rev_opt,
       CASE 
           WHEN tt2.bg_own=1 THEN IFNULL(t3.payout, 0)
           WHEN tt2.bg_own=0 AND tt2.target=2 THEN t1.spent_cpc_raw
           ELSE IFNULL(t1.spent_cpm, 0)
       END AS rev_real
FROM
  (SELECT tag_id,
          ad_id, 
	  browser,    
	  DATE,       
          SUM(imp) AS imp,
					   
                       SUM(click_raw) AS click_raw,
                       SUM(click_landing) AS click_landing,
                       ROUND(SUM(spent_cpm)/1000,0) AS spent_cpm,
                       SUM(spent_cpc_raw) AS spent_cpc_raw,
                       SUM(spent_cpc_landing) AS spent_cpc_landing
   FROM stats_ads_tags_browser_by_node_hour
   WHERE DATE={date}

   GROUP BY tag_id, ad_id,browser, DATE) t1
LEFT JOIN ads t2 ON t1.ad_id= t2.id
LEFT JOIN `campaigns` tt2 ON t2.campaign_id=tt2.id
LEFT JOIN
  (SELECT tag_id,
          ad_id,
          browser,
          SUM(payout) AS payout,
          DATE
   FROM conversions_click
   WHERE DATE={date}
   GROUP BY tag_id, ad_id, browser
	) t3 ON t1.tag_id=t3.tag_id
AND t1.browser = t3.browser
AND t1.ad_id=t3.ad_id
AND t1.date=t3.date
    """,
        'index': ['ad_id', 'tag_id', 'date', 'browser'],
        'table_name': 'stats_ads_tags_browser_by_node_hour'
    },
    {
        'sql': """
SELECT 	tt1.tag_id, 
	tt1.date, 
	1 AS source_id, 
	tt1.browser, 
	IFNULL(tt1.request,0) AS request, 
	IFNULL(tt1.paid,0) AS paid, 
	IFNULL(t1.imp,0) AS imp, 
	IFNULL(t1.click_raw,0) AS click_raw, 
	IFNULL(t1.click_landing,0) AS click_landing, 
	IFNULL(t1.click_raw,0) AS click, 
	IFNULL(t1.spent_cpm,0) AS spent_cpm, 
	IFNULL(t1.spent_cpc_raw,0) AS spent_cpc_raw, 
	IFNULL(t1.spent_cpc_landing,0) AS spent_cpc_landing, 
       IFNULL(t1.spent,0) AS spent,
       IFNULL(t1.rev_opt, 0) AS rev_opt,
       IFNULL(t1.rev_real, 0) AS rev_real
	
FROM  (
SELECT tag_id, 
	browser,
	DATE,
       SUM(request) AS request,
       SUM(paid) AS paid
   FROM stats_tags_browser_by_node_hour 
   WHERE DATE={date}
   GROUP BY tag_id,browser,DATE
)
 tt1 LEFT JOIN
(SELECT tag_id,
	browser,
	SUM(imp) AS imp,
	SUM(click_raw) AS click_raw,
	SUM(click_landing) AS click_landing,
	SUM(spent_cpm) AS spent_cpm,
	SUM(spent_cpc_raw) AS spent_cpc_raw,
	SUM(spent_cpc_landing) AS spent_cpc_landing,
	SUM(spent) AS spent,
        SUM(rev_opt) AS rev_opt,
        SUM(rev_real) AS rev_real
FROM stats_ads_tags_browser WHERE DATE={date}
   
GROUP BY tag_id,browser)  t1 ON  tt1.tag_id = t1.tag_id AND tt1.browser = t1.browser
    """,
        'index': ['tag_id', 'date', 'browser'],
        'table_name': 'stats_tags_browser_by_node_hour'
    },
    {
        'sql': """
SELECT   t2.domain_id AS did,
  t1.tag_id,
  t1.location1, 
  t1.device1, 
  t1.device2, 
  t1.date, 
  IFNULL(t1.request,0) AS request, 
  IFNULL(t1.paid,0) AS paid, 
  IFNULL(t1.imp,0) AS imp, 
  IFNULL(t1.click_raw,0) AS click_raw, 
  IFNULL(t1.click_landing,0) AS click_landing, 
  IFNULL(t1.click_raw,0) AS click,
  IFNULL(t1.spent_cpm,0) AS spent_cpm,
  IFNULL(t1.spent_cpc_raw,0) AS spent_cpc_raw, 
  IFNULL(t1.spent_cpc_landing,0) AS spent_cpc_landing, 
  (IFNULL(t1.spent_cpm,0) + IFNULL(t1.spent_cpc_raw,0)) AS spent,
  
  IFNULL(t3.payout,0) AS rev_opt,
  (IFNULL(t3.payout,0) + IFNULL(t1.spent_cpm,0) + IFNULL(t1.spent_cpc_raw,0)) AS rev_real,
  IFNULL(t4.tier,0) AS tier, 
  UNIX_TIMESTAMP() AS updated_time
FROM
  (SELECT tag_id,     
       location1,
       device1,
       device2,
       DATE, 
       SUM(imp) AS imp,
       SUM(request) AS request,
       SUM(paid) AS paid,
       SUM(click_raw) AS click_raw,
       SUM(click_landing) AS click_landing,
       ROUND(SUM(spent_cpm)/1000,0) AS spent_cpm,
       SUM(spent_cpc_raw) AS spent_cpc_raw,
       SUM(spent_cpc_landing) AS spent_cpc_landing,
       tier,NOW() AS updated_time
   FROM stats_tags_inventories_by_node_hour
   WHERE DATE={date}

   GROUP BY tag_id,location1,device1,device2,DATE) t1
LEFT JOIN tags t2 ON t1.tag_id= t2.id
LEFT JOIN
  (SELECT tag_id,
      location1,
      device1,
      device2,
          SUM(payout) AS payout,
          DATE
   FROM conversions_click
   WHERE DATE={date}
   GROUP BY  tag_id,location1,device1,device2
  ) t3 ON t1.tag_id=t3.tag_id
AND t1.location1 = t3.location1
AND t1.device1 = t3.device1
AND t1.device2 = t3.device2
AND t1.date=t3.date
LEFT JOIN `targeting` t4 ON t1.location1=t4.id
    """,
        'index': ['tag_id', 'date', 'location1', 'device1', 'device2'],
        'table_name': 'stats_tags_inventories_by_node_hour'
    },
    {
        'sql': """
SELECT 
	t1.tag_id, 
	t1.`campaign_id`, 
	t1.`date`, 
	IFNULL(t1.`paid`,0) AS paid, 
	IFNULL(t1.`imp`,0) AS imp, 
	2 AS `source_id`, 
	IFNULL(t1.`request`,0) AS request, 
	IFNULL(t1.`click_raw`,0) AS click_raw, 
	IFNULL(t1.`click_landing`,0) AS click_landing, 
	IFNULL(t1.click_raw,0) AS click, 
	IFNULL(t1.spent_cpm,0) AS spent_cpm, 
	IFNULL(t1.spent_cpc_raw,0) AS spent_cpc_raw, 
	IFNULL(t1.spent_cpc_landing,0) AS spent_cpc_landing, 
	 CASE tt2.target 
	   WHEN  2 THEN spent_cpc_raw
	   ELSE IFNULL(t1.spent_cpm, 0) 
       END AS spent, 
	IFNULL(t3.payout,0) AS rev_opt, 
	CASE 
           WHEN tt2.bg_own=1 THEN IFNULL(t3.payout, 0)
           WHEN tt2.bg_own=0 AND tt2.target=2 THEN t1.spent_cpc_raw
           ELSE IFNULL(t1.spent_cpm, 0)
       END AS rev_real
FROM
  (SELECT tag_id,
	  campaign_id,    
	  DATE,       
          SUM(imp) AS imp,
          SUM(paid) AS paid,
          SUM(request) AS request,
					   
                       SUM(click_raw) AS click_raw,
                       SUM(click_landing) AS click_landing,
                       ROUND(SUM(spent_cpm)/1000,0) AS spent_cpm,
                       SUM(spent_cpc_raw) AS spent_cpc_raw,
                       SUM(spent_cpc_landing) AS spent_cpc_landing
   FROM stats_ads_tags_campaign_by_node_hour
   WHERE DATE={date}

   GROUP BY tag_id, campaign_id, DATE) t1
LEFT JOIN `campaigns` tt2 ON t1.campaign_id=tt2.id
LEFT JOIN
  (SELECT tag_id,
          campaign_id,
          SUM(payout) AS payout,
          DATE
   FROM conversions_click
   WHERE DATE={date}
   GROUP BY tag_id, campaign_id
	) t3 ON t1.tag_id=t3.tag_id
AND t1.campaign_id = t3.campaign_id
AND t1.date=t3.date
    """,
        'index': ['tag_id', 'date', 'location1', 'device1', 'device2'],
        'table_name': 'stats_tags_inventories_by_node_hour'
    },
    {
        'sql': """
SELECT 
	t1.tag_id, 
	t1.`campaign_id`, 
	t1.`date`, 
	IFNULL(t1.`paid`,0) AS paid, 
	IFNULL(t1.`imp`,0) AS imp, 
	2 AS `source_id`, 
	IFNULL(t1.`request`,0) AS request, 
	IFNULL(t1.`click_raw`,0) AS click_raw, 
	IFNULL(t1.`click_landing`,0) AS click_landing, 
	IFNULL(t1.click_raw,0) AS click, 
	IFNULL(t1.spent_cpm,0) AS spent_cpm, 
	IFNULL(t1.spent_cpc_raw,0) AS spent_cpc_raw, 
	IFNULL(t1.spent_cpc_landing,0) AS spent_cpc_landing, 
	 CASE tt2.target 
	   WHEN  2 THEN spent_cpc_raw
	   ELSE IFNULL(t1.spent_cpm, 0) 
       END AS spent, 
	IFNULL(t3.payout,0) AS rev_opt, 
	CASE 
           WHEN tt2.bg_own=1 THEN IFNULL(t3.payout, 0)
           WHEN tt2.bg_own=0 AND tt2.target=2 THEN t1.spent_cpc_raw
           ELSE IFNULL(t1.spent_cpm, 0)
       END AS rev_real
FROM
  (SELECT tag_id,
	  campaign_id,    
	  DATE,       
          SUM(imp) AS imp,
          SUM(paid) AS paid,
          SUM(request) AS request,
					   
                       SUM(click_raw) AS click_raw,
                       SUM(click_landing) AS click_landing,
                       ROUND(SUM(spent_cpm)/1000,0) AS spent_cpm,
                       SUM(spent_cpc_raw) AS spent_cpc_raw,
                       SUM(spent_cpc_landing) AS spent_cpc_landing
   FROM stats_ads_tags_campaign_by_node_hour
   WHERE DATE={date}

   GROUP BY tag_id, campaign_id, DATE) t1
LEFT JOIN `campaigns` tt2 ON t1.campaign_id=tt2.id
LEFT JOIN
  (SELECT tag_id,
          campaign_id,
          SUM(payout) AS payout,
          DATE
   FROM conversions_click
   WHERE DATE={date}
   GROUP BY tag_id, campaign_id
	) t3 ON t1.tag_id=t3.tag_id
AND t1.campaign_id = t3.campaign_id
AND t1.date=t3.date
    """,
        'index': ['tag_id', 'date', 'campaign_id'],
        'table_name': 'stats_ads_tags_campaign_by_node_hour'
    },
    {
        'sql': """
SELECT 
	t1.tag_id, 
	t1.`campaign_id`, 
	t1.`date`, 
	IFNULL(t1.`paid`,0) AS paid, 
	IFNULL(t1.`imp`,0) AS imp, 
	2 AS `source_id`, 
	IFNULL(t1.`request`,0) AS request, 
	IFNULL(t1.`click_raw`,0) AS click_raw, 
	IFNULL(t1.`click_landing`,0) AS click_landing, 
	IFNULL(t1.click_raw,0) AS click, 
	IFNULL(t1.spent_cpm,0) AS spent_cpm, 
	IFNULL(t1.spent_cpc_raw,0) AS spent_cpc_raw, 
	IFNULL(t1.spent_cpc_landing,0) AS spent_cpc_landing, 
	 CASE tt2.target 
	   WHEN  2 THEN spent_cpc_raw
	   ELSE IFNULL(t1.spent_cpm, 0) 
       END AS spent, 
	IFNULL(t3.payout,0) AS rev_opt, 
	CASE 
           WHEN tt2.bg_own=1 THEN IFNULL(t3.payout, 0)
           WHEN tt2.bg_own=0 AND tt2.target=2 THEN t1.spent_cpc_raw
           ELSE IFNULL(t1.spent_cpm, 0)
       END AS rev_real
FROM
  (SELECT tag_id,
	  campaign_id,    
	  DATE,       
          SUM(imp) AS imp,
          SUM(paid) AS paid,
          SUM(request) AS request,

                       SUM(click_raw) AS click_raw,
                       SUM(click_landing) AS click_landing,
                       ROUND(SUM(spent_cpm)/1000,0) AS spent_cpm,
                       SUM(spent_cpc_raw) AS spent_cpc_raw,
                       SUM(spent_cpc_landing) AS spent_cpc_landing
   FROM stats_ads_tags_campaign_by_node_hour
   WHERE DATE={date}

   GROUP BY tag_id, campaign_id, DATE) t1
LEFT JOIN `campaigns` tt2 ON t1.campaign_id=tt2.id
LEFT JOIN
  (SELECT tag_id,
          campaign_id,
          SUM(payout) AS payout,
          DATE
   FROM conversions_click
   WHERE DATE={date}
   GROUP BY tag_id, campaign_id
	) t3 ON t1.tag_id=t3.tag_id
AND t1.campaign_id = t3.campaign_id
AND t1.date=t3.date
    """,
        'index': ['tag_id', 'date', 'ad_id', 'location1', 'location2', 'device1', 'device2'],
        'table_name': 'stats_ads_performance_by_node_hour'
    }
]
