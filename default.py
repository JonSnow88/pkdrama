# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Thanks to the Authors of the base code
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.pkdramas'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCdmkPG3FG48A27-PrD-lC8A" 	# A Plus Entertainment
YOUTUBE_CHANNEL_ID_2 = "UC2m98kh188cg_9x248IZM9A" 	# Aaj Entertainment
YOUTUBE_CHANNEL_ID_3 = "UC4JCksJF76g_MdzPVBJoC3Q" 	# ARY Digital
YOUTUBE_CHANNEL_ID_4 = "UCVswAdjz8Ho0y24eVarY5wg" 	# ARY Zindagi
YOUTUBE_CHANNEL_ID_5 = "UCecuhrESo2Pit4YDg8CQiGg" 	# ATV
YOUTUBE_CHANNEL_ID_6 = "UCU1r97baEf3JJI5fY6NtMpA" 	# Express Entertainment
YOUTUBE_CHANNEL_ID_7 = "UCe9JSDmyqNgA_l2BzGHq1Ug" 	# Geo TV
YOUTUBE_CHANNEL_ID_8 = "UCEeEQxm6qc_qaTE7qTV5aLQ" 	# Hum TV
YOUTUBE_CHANNEL_ID_9 = "UCatkw-24OJitQmOVKPhQk1g" 	# TVOne
YOUTUBE_CHANNEL_ID_10 = "UCBS11rSNRLPCVJ1tZZ4GaRQ" 	# TVOne Classics
YOUTUBE_CHANNEL_ID_11 = "UCNs8nUP7pDBA9tIKA3NwzoA" 	# Urdu1TV
YOUTUBE_CHANNEL_ID_12 = "UCyFbHB68DazkUxdq2WvPDfQ" 	# Best Pakistani Dramas



# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title=" A Plus Entertainment",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-dClaLJXn4SM/AAAAAAAAAAI/AAAAAAAAAAA/Np7qYaUtR3I/s300-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Aaj Entertainment",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-MuxMxskrVmg/AAAAAAAAAAI/AAAAAAAAAAA/gKVuxGCuhd4/s300-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ARY Digital",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-xmooBxnvMJk/AAAAAAAAAAI/AAAAAAAAAAA/RmElKyHWO-g/s300-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="ARY Zindagi",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-t0pmLh-JJWk/AAAAAAAAAAI/AAAAAAAAAAA/quQWHxlktOg/s300-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="ATV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/-IxtM0lsi93c/AAAAAAAAAAI/AAAAAAAAAAA/u76I6cg2Spw/s300-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Express Entertainment",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-WDinAoP2URw/AAAAAAAAAAI/AAAAAAAAAAA/QLtH_Cshd_c/s300-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Geo TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/-9Ykf4Zc9GxQ/AAAAAAAAAAI/AAAAAAAAAAA/mCXr1jU-9Q8/s300-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Hum TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://yt3.ggpht.com/-8nn2mPhObBg/AAAAAAAAAAI/AAAAAAAAAAA/nO8qj4CRQL8/s300-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="TVOne",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/-Iq_HXN8Ic2c/AAAAAAAAAAI/AAAAAAAAAAA/s2Ol-7ezyGc/s300-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="",
        folder=True )
				
    plugintools.add_item( 
        #action="", 
        title="TVOne Classics",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/-2kZ_GMjQkQs/AAAAAAAAAAI/AAAAAAAAAAA/zOFQH92UMeU/s300-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="",
        folder=True )
				
    plugintools.add_item( 
        #action="", 
        title="Urdu1TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://yt3.ggpht.com/-7tIqCKyQPv4/AAAAAAAAAAI/AAAAAAAAAAA/aZRdS_D-sjY/s300-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="",
        folder=True )
				
    plugintools.add_item( 
        #action="", 
        title="Best Pakistani Dramas",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://yt3.ggpht.com/-6gr0JVoCLbE/AAAAAAAAAAI/AAAAAAAAAAA/mnggo9xO50g/s300-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="",
        folder=True )
				
run()
