#merger.addAction( "SectionIntelligence", GraphQuery(("TagName",), Arg = ("AttributeName","AtributeVale") )
"""<TagName AttributeName = AtributeVale></TagName>"""

merger.addAction( "CopyValue", GraphQuery(("general","systemtotaluptime")) )
merger.addAction( "CopySection", GraphQuery(("myvideos",)) )
merger.addAction( "CopySection", GraphQuery(("mymusic",)), BlackList = [ GraphQuery(("playlist","repeat")), GraphQuery(("playlist","shuffle")) ] )
merger.addAction( "CopySection", GraphQuery(("viewstates",)) )

#Policy = QUERY_POLICY_ONLY_NEW GraphQuery execute only on new config. I think it`s useful for deleting node in new config
#Policy = QUERY_POLICY_BOTH GraphQuery execute on both xml files
merger.addAction( "DeleteSection", GraphQuery(("viewstates","musicnavalbums")), Policy = QUERY_POLICY_ONLY_NEW )

merger.addAction( "CopySection", GraphQuery(("content","test"), Content = "22222", BackStep = 1) )


