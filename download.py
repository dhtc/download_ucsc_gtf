import requests
import sys
genome=sys.argv[1]
s = requests.Session()
data={
'hgsid':'728237695_Ylr8ZUjsrhGDLHSBVCKl5icee4XX',
'jsh_pageVertPos':'0',
'clade':'mammal',
'org':'Human',
'db':genome,
'hgta_group':'genes',
'hgta_track':'refSeqComposite',
'hgta_table':'ncbiRefSeq',
'hgta_regionType':'genome',
'position':' chr15'':''73,572,277-74,047,170',
'hgta_outputType':'bed',
'boolshad.sendToGalaxy':'0',
'boolshad.sendToGreat':'0',
'boolshad.sendToGenomeSpace':'0',
'hgta_outFileName':'hg19.bed',
'hgta_compressType':'none',
'hgta_doTopSubmit':'get output'}
headers={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'hguid=661355781_012DBmvXkHSYKl2tpfuZp0aoHZNS; _ga=GA1.2.431634720.1549939374; hguid.genome-japan=527118679_VPFavVO6g3DDkzkKLhE16HyrEZ3L; redirect=manual; _gid=GA1.2.1614034732.1559279785; _gat=1',
'Host':'genome.ucsc.edu',
'Referer':'http://genome.ucsc.edu/cgi-bin/hgTables',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}
p=s.post('http://genome.ucsc.edu/cgi-bin/hgTables',data=data,headers=headers)

params={
'hgsid':'728237695_Ylr8ZUjsrhGDLHSBVCKl5icee4XX',
'boolshad.hgta_printCustomTrackHeaders':'0',
'hgta_ctName':'tb_ncbiRefSeq',
'hgta_ctDesc':'table browser query on ncbiRefSeq',
'hgta_ctVis':'pack',
'hgta_ctUrl':'',
'fbQual':'whole',
'fbUpBases':'200',
'fbExonBases':'0',
'fbIntronBases':'0',
'fbDownBases':'200',
'hgta_doGetBed':'get BED'}

g=s.get('http://genome.ucsc.edu/cgi-bin/hgTables',params=params)
with open(genome+'.bed','w')as f:
	f.write(g.text)