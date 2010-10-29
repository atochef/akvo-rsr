table = 'oembed_storedprovider'
fields = ['id', 'endpoint_url', 'regex', 'wildcard_regex', 'resource_type', 'active', 'provides', 'scheme_url']
#default item format: "fieldname":("type", "value")
default = {}
records = [
[1L, u'http://www.flickr.com/services/oembed/', u'http://\\S*?flickr.com/\\S*', u'http://*.flickr.com/*', u'photo', 1, 0, u'']
[2L, u'http://lab.viddler.com/services/oembed/', u'http://\\S*?viddler.com/\\S*', u'http://*.viddler.com/*', u'video', 1, 0, u'']
[3L, u'http://qik.com/api/oembed.json', u'http://qik.com/\\S*', u'http://qik.com/*', u'video', 1, 0, u'']
[4L, u'http://api.pownce.com/2.1/oembed.json', u'http://\\S*?pownce.com/\\S*', u'http://*.pownce.com/*', u'video', 1, 0, u'']
[5L, u'http://revision3.com/api/oembed/', u'http://\\S*?revision3.com/\\S*', u'http://*.revision3.com/*', u'video', 1, 0, u'']
[6L, u'http://api.embed.ly/v1/api/oembed', u'http://\\S*.collegehumor.com/video:\\S*', u'http://*.collegehumor.com/video:*', u'video', 0, 0, u'']
[7L, u'http://api.embed.ly/v1/api/oembed', u'http://\\S*.funnyordie.com/videos/\\S*', u'http://*.funnyordie.com/videos/*', u'video', 0, 0, u'']
[8L, u'http://api.embed.ly/v1/api/oembed', u'http://video.google.com/videoplay?\\S*', u'http://video.google.com/videoplay?*', u'video', 0, 0, u'']
[9L, u'http://api.embed.ly/v1/api/oembed', u'http://www.hulu.com/watch/\\S*', u'http://www.hulu.com/watch/*', u'video', 0, 0, u'']
[10L, u'http://api.embed.ly/v1/api/oembed', u'http://\\S*.metacafe.com/watch/\\S*', u'http://*.metacafe.com/watch/*', u'video', 0, 0, u'']
[11L, u'http://api.embed.ly/v1/api/oembed', u'http://twitter.com/\\S*/statuses/\\S*', u'http://twitter.com/*/statuses/*', u'rich', 0, 0, u'']
[12L, u'http://oohembed.com/oohembed/', u'http://\\S*.wikipedia.org/wiki/\\S*', u'http://*.wikipedia.org/wiki/*', u'rich', 1, 0, u'']
[13L, u'http://www.youtube.com/oembed', u'http://\\S*.youtube.com/watch\\S*', u'http://www.youtube.com/watch*', u'video', 1, 0, u'']
[14L, u'http://vimeo.com/api/oembed.json', u'http://vimeo.com/\\S*', u'http://vimeo.com/*', u'video', 1, 0, u'']
[15L, u'http://api.embed.ly/v1/api/oembed', u'http://www.slideshare.net/\\S*/\\S*', u'http://www.slideshare.net/*/*', u'rich', 0, 0, u'']
[16L, u'http://api.embed.ly/v1/api/oembed', u'http://\\S*.scribd.com/doc/\\S*', u'http://*.scribd.com/doc/*', u'rich', 0, 0, u'']
[17L, u'http://api.embed.ly/v1/api/oembed', u'http://screenr.com/\\S*', u'http://screenr.com/*', u'video', 0, 0, u'']
[18L, u'http://api.embed.ly/v1/api/oembed', u'http://www.5min.com/Video/\\S*', u'http://www.5min.com/Video/*', u'video', 0, 0, u'']
[19L, u'http://api.embed.ly/v1/api/oembed', u'http://www.howcast.com/videos/\\S*', u'http://www.howcast.com/videos/*', u'video', 0, 0, u'']
[20L, u'http://api.embed.ly/v1/api/oembed', u'(http://\\S*?screencast.com/\\S*/media/\\S*|http://\\S*?screencast.com/t/\\S*)', u'http://*.screencast.com/*/media/*', u'video', 0, 0, u'']
[21L, u'http://api.embed.ly/v1/api/oembed', u'http://www.clearspring.com/widgets/\\S*', u'http://www.clearspring.com/widgets/*', u'rich', 0, 0, u'']
[22L, u'http://api.embed.ly/v1/api/oembed', u'(http://my.opera.com/\\S*/albums/show.dml\\?id=\\S*|http://my.opera.com/\\S*/albums/showpic.dml\\?album=\\S*&picture=\\S*)', u'http://my.opera.com/*/albums/showpic.dml?album=*&picture=*)', u'video', 0, 0, u'']
[23L, u'http://api.embed.ly/v1/api/oembed', u'http://\\S*yfrog.\\S*/\\S*', u'http://*.yfrog.*/*', u'photo', 0, 0, u'']
[24L, u'http://api.embed.ly/v1/api/oembed', u'http://tweetphoto.com/\\S*', u'http://tweetphoto.com/*', u'photo', 0, 0, u'']
[25L, u'http://api.embed.ly/v1/api/oembed', u'http://\\S*twitpic.com/\\S*', u'http://*.twitpic.com/*', u'photo', 0, 0, u'']
[26L, u'http://api.embed.ly/v1/api/oembed', u'http://\\S*imgur.com/\\S*', u'http://*.imgur.com/*', u'photo', 0, 0, u'']
[27L, u'http://api.embed.ly/v1/api/oembed', u'http://twitgoo.com/\\S*', u'http://twitgoo.com/*', u'photo', 0, 0, u'']
[28L, u'http://api.embed.ly/v1/api/oembed', u'(http://i\\S*.photobucket.com/albums/\\S*|http://gi\\S*.photobucket.com/groups/\\S*)', u'http://*.photobucket.com/albums/*', u'photo', 0, 0, u'']
[29L, u'http://api.embed.ly/v1/api/oembed', u'http://phodroid.com/\\S*/\\S*/\\S*', u'http://phodroid.com/*/*/*', u'photo', 0, 0, u'']
[30L, u'http://api.embed.ly/v1/api/oembed', u'http://xkcd.com/\\S*', u'http://xkcd.com/*', u'photo', 0, 0, u'']
[31L, u'http://api.embed.ly/v1/api/oembed', u'http://\\S*?23hq.com/\\S*/photo/\\S*', u'http://*.23hq.com/*/photo/*', u'photo', 0, 0, u'']
[32L, u'http://api.embed.ly/v1/api/oembed', u'(http://\\S*amazon.\\S*/gp/product/\\S*|http://\\S*amazon.\\S*/\\S*/dp/\\S*|http://\\S*amazon.\\S*/dp/\\S*|http://\\S*amazon.\\S*/o/ASIN/\\S*|http://\\S*amazon.\\S*/gp/offer-listing/\\S*|http://\\S*amazon.\\S*/\\S*/ASIN/\\S*|http://\\S*amazon.\\S*/gp/product/images/\\S*)', u'http://*.amazon.*/*', u'rich', 0, 0, u'']
[33L, u'http://api.embed.ly/v1/api/oembed', u'http://www.veoh.com/\\S*/watch/\\S*', u'http://www.veoh.com/*/watch/*', u'video', 0, 0, u'']
[34L, u'http://api.embed.ly/v1/api/oembed', u'http://\\S*justin.tv/\\S*', u'http://*.justin.tv/*', u'video', 0, 0, u'']
[35L, u'http://api.embed.ly/v1/api/oembed', u'http://www.ustream.tv/(recorded|channel)/\\S*', u'http://www.ustream.tv/*/*', u'video', 0, 0, u'']
[36L, u'http://api.embed.ly/v1/api/oembed', u'(http://\\S*.dailymotion.com/video/\\S*|http://\\S*.dailymotion.com/\\S*/video/\\S*)', u'http://*.dailymotion.com/*/video/*', u'video', 0, 0, u'']
[37L, u'http://api.embed.ly/v1/api/oembed', u'http://www.twitvid.com/\\S*', u'http://www.twitvid.com/*', u'video', 0, 0, u'']
[38L, u'http://api.embed.ly/v1/api/oembed', u'http://www.break.com/\\S*/\\S*', u'http://www.break.com/*/*', u'video', 0, 0, u'']
[39L, u'http://api.embed.ly/v1/api/oembed', u'http://(www|vids).myspace.com/index.cfm\\?fuseaction=\\S*&videoid\\S*', u'http://*.myspace.com/index.cfm?fuseaction=*&videoid=*', u'video', 0, 0, u'']
[40L, u'http://api.embed.ly/v1/api/oembed', u'http://\\S*blip.tv/file/\\S*', u'http://*.blip.tv/file/*', u'video', 0, 0, u'']
[41L, u'http://api.embed.ly/v1/api/oembed', u'http://\\S*revver.com/video/\\S*', u'http://*.revver.com/video/*', u'video', 0, 0, u'']
[42L, u'http://api.embed.ly/v1/api/oembed', u'(http://video.yahoo.com/watch/\\S*/\\S*|http://video.yahoo.com/network/\\S*)', u'http://video.yahoo.com/*', u'video', 0, 0, u'']
[43L, u'http://api.embed.ly/v1/api/oembed', u'http://\\S*?liveleak.com/view?\\S*', u'http://*.liveleak.com/view?*', u'video', 0, 0, u'']
[44L, u'http://api.embed.ly/v1/api/oembed', u'http://animoto.com/(play|s)/\\S*', u'http://animoto.com/*', u'video', 0, 0, u'']
[45L, u'http://api.embed.ly/v1/api/oembed', u'http://dotsub.com/view/\\S*', u'http://dotsub.com/view/*', u'video', 0, 0, u'']
[46L, u'http://api.embed.ly/v1/api/oembed', u'http://soundcloud.com/\\S*', u'http://soundcloud.com/*', u'video', 0, 0, u'']
[47L, u'http://api.embed.ly/v1/api/oembed', u'http://www.lala.com/#*(album|song)/\\S*', u'http://www.lala.com/*/*', u'rich', 0, 0, u'']
[48L, u'http://api.embed.ly/v1/api/oembed', u'(http://movieclips.com/watch/\\S*/\\S*/|http://movieclips.com/watch/\\S*/\\S*/\\S*/\\S*)', u'http://movieclips.com/watch/*/*)', u'video', 0, 0, u'']
[49L, u'http://api.embed.ly/v1/api/oembed', u'http://\\S*crackle.com/c/\\S*', u'http://*.crackle.com/c/*', u'video', 0, 0, u'']
[50L, u'http://api.embed.ly/v1/api/oembed', u'http://www.fancast.com/\\S*/videos', u'http://www.fancast.com/*/videos', u'video', 0, 0, u'']
[51L, u'http://api.embed.ly/v1/api/oembed', u'http://www.ted.com/talks/\\S*.html', u'http://www.ted.com/talks/*', u'video', 0, 0, u'']
[52L, u'http://api.embed.ly/v1/api/oembed', u'http://\\S*omnisio.com/\\S*', u'http://*.omnisio.com/*', u'video', 0, 0, u'']
[53L, u'http://api.embed.ly/v1/api/oembed', u'http://\\S*nfb.ca/film/\\S*', u'http://*.nfb.ca/film/*', u'video', 0, 0, u'']
[54L, u'http://api.embed.ly/v1/api/oembed', u'(http://www.thedailyshow.com/(watch|full-episodes)/\\S*|http://www.thedailyshow.com/collection/\\S*/\\S*/\\S*)', u'http://www.thedailyshow.com/*', u'video', 0, 0, u'']
[55L, u'http://api.embed.ly/v1/api/oembed', u'http://movies.yahoo.com/movie/\\S*/(video|info|trailer)/\\S*', u'http://movies.yahoo.com/movie/*', u'video', 0, 0, u'']
[56L, u'http://api.embed.ly/v1/api/oembed', u'http://www.colbertnation.com/(the-colbert-report-collections|full-episodes|the-colbert-report-videos)/\\S*', u'http://www.colbertnation.com/*', u'video', 0, 0, u'']
[57L, u'http://api.embed.ly/v1/api/oembed', u'http://www.comedycentral.com/videos/index.jhtml?\\S*', u'http://www.comedycentral.com/videos/index.jhtml?*', u'video', 0, 0, u'']
[58L, u'http://api.embed.ly/v1/api/oembed', u'http://\\S*theonion.com/video/\\S*', u'http://*.theonion.com/video/*', u'video', 0, 0, u'']
[59L, u'http://api.embed.ly/v1/api/oembed', u'http://wordpress.tv/\\S*/\\S*/\\S*/\\S*/', u'http://wordpress.tv/*/*/*/*/', u'video', 0, 0, u'']
[60L, u'http://api.embed.ly/v1/api/oembed', u'http://www.traileraddict.com/(trailer|clip|poster)/\\S*', u'http://www.traileraddict.com/*', u'video', 0, 0, u'']
[61L, u'http://api.embed.ly/v1/api/oembed', u'http://www.escapistmagazine.com/videos/\\S*', u'http://www.escapistmagazine.com/videos/*', u'video', 0, 0, u'']
]