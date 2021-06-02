import requests
from bs4 import BeautifulSoup
print(' Hey there..! Checking 86th BMA-issb candidate statistics. Please wait' + '.'*20)

res = requests.get('https://www.issb-bd.org/calluplist').text
soup = BeautifulSoup(res, 'lxml')

contents = soup.find_all('div', class_ = 'col-md-12')

#turn the html into simple text
for content in contents:
	roll_string = (content.text)

#convert the content from a whole string to each word into list
def Convert(string):
    li = list(string.split(","))
    return li

roll_list = (Convert(roll_string))

# using list comprehension + startswith()
# Prefix Separation to separate the 86th bma batch from others
start_letter = ' 86'
with_s = [x for x in roll_list if x.startswith(start_letter)]

#remove the space in front of the strings in the list
final_list=[]
for i in with_s:
	final_list.append(i[1:])

#remove a mistake of the editors
final_list.pop(0)

#create the written passed candidate list

Board_1 = ['86010001', '86010053', '86010113', '86010146', '86010188', '86010221', '86010257', '86010004', '86010057', '86010115', '86010151', '86010192', '86010222', '86010268', '86010005', '86010061', '86010116', '86010156', '86010195', '86010224', '86010269', '86010006', '86010064', '86010117', '86010157', '86010205', '86010230', '86010272', '86010020', '86010069', '86010118', '86010165', '86010212', '86010237', '86010273', '86010022', '86010095', '86010121', '86010168', '86010213', '86010239', '86010274', '86010027', '86010105', '86010131', '86010170', '86010214', '86010240', '86010279', '86010038', '86010108', '86010137', '86010175', '86010217', '86010246', '86010281', '86010039', '86010109', '86010138', '86010176', '86010218', '86010251', '86010286', '86010047', '86010111', '86010140', '86010177', '86010220', '86010252', '86010287', '86010293', '86010301', '86010313', '86010323', '86010335', '86010343', '86010347', '86010299', '86010312', '86010317', '86010325', '86010337', '86010345']

Board_2 = ['86020001', '86020041', '86020074', '86020097', '86020112', '86020157', '86020204', '86020008', '86020047', '86020078', '86020098', '86020124', '86020159', '86020209', '86020019', '86020048', '86020085', '86020099', '86020125', '86020160', '86020212', '86020023', '86020049', '86020086', '86020102', '86020129', '86020167', '86020214', '86020030', '86020050', '86020087', '86020104', '86020130', '86020174', '86020216', '86020032', '86020051', '86020088', '86020105', '86020134', '86020178', '86020221', '86020033', '86020057', '86020089', '86020106', '86020143', '86020180', '86020222', '86020036', '86020061', '86020092', '86020107', '86020144', '86020185', '86020224', '86020039', '86020069', '86020095', '86020108', '86020147', '86020192', '86020225', '86020040', '86020070', '86020096', '86020110', '86020153', '86020196', '86020228', '86020237', '86020254', '86020281', '86020300', '86020322', '86020329', '86020351', '86020240', '86020258', '86020283', '86020301', '86020326', '86020339', '86020356', '86020243', '86020280', '86020292', '86020302', '86020328', '86020347', '86020358', '86020248']

Board_3 = ['86030002', '86030050', '86030092', '86030126', '86030160', '86030216', '86030273', '86030008', '86030052', '86030100', '86030128', '86030164', '86030220', '86030282', '86030012', '86030061', '86030102', '86030131', '86030165', '86030224', '86030284', '86030014', '86030062', '86030108', '86030137', '86030167', '86030247', '86030291', '86030020', '86030065', '86030110', '86030145', '86030173', '86030259', '86030293', '86030031', '86030069', '86030111', '86030151', '86030178', '86030261', '86030294', '86030032', '86030076', '86030112', '86030153', '86030186', '86030262', '86030296', '86030033', '86030078', '86030113', '86030155', '86030191', '86030267', '86030297', '86030042', '86030081', '86030115', '86030156', '86030206', '86030268', '86030300', '86030047', '86030091', '86030122', '86030158', '86030215', '86030270', '86030307', '86030314', '86030320', '86030334', '86030340', '86030348', '86030355', '86030318', '86030331', '86030335', '86030342', '86030351', '86030356']

Board_4 = ['86040003', '86040021', '86040041', '86040055', '86040070', '86040084', '86040104', '86040010', '86040022', '86040043', '86040056', '86040071', '86040085', '86040106', '86040011', '86040023', '86040045', '86040057', '86040072', '86040087', '86040110', '86040012', '86040024', '86040046', '86040058', '86040075', '86040089', '86040111', '86040013', '86040027', '86040047', '86040059', '86040076', '86040091', '86040112', '86040014', '86040028', '86040048', '86040061', '86040078', '86040093', '86040115', '86040015', '86040029', '86040049', '86040062', '86040079', '86040094', '86040117', '86040016', '86040030', '86040050', '86040064', '86040080', '86040095', '86040120', '86040017', '86040031', '86040051', '86040066', '86040082', '86040097', '86040123', '86040019', '86040038', '86040052', '86040069', '86040083', '86040103', '86040124', '86040127', '86040144', '86040162', '86040191', '86040212', '86040246', '86040272', '86040128', '86040148', '86040163', '86040194', '86040213', '86040247', '86040275', '86040131', '86040150', '86040165', '86040195', '86040215', '86040248', '86040277', '86040132', '86040151', '86040167', '86040197', '86040225', '86040250', '86040278', '86040135', '86040152', '86040171', '86040198', '86040230', '86040254', '86040279', '86040136', '86040153', '86040173', '86040202', '86040231', '86040256', '86040281', '86040138', '86040154', '86040178', '86040205', '86040234', '86040258', '86040283', '86040141', '86040155', '86040187', '86040207', '86040235', '86040263', '86040286', '86040142', '86040158', '86040189', '86040209', '86040236', '86040266', '86040294', '86040143', '86040159', '86040190', '86040210', '86040242', '86040269', '86040295', '86040297', '86040311', '86040321', '86040337', '86040343', '86040351', '86040358', '86040302', '86040316', '86040327', '86040342', '86040350', '86040356', '86040361', '86040307', '86040317']

Board_5 = ['86050002', '86050021', '86050041', '86050057', '86050075', '86050130', '86050152', '86050003', '86050022', '86050042', '86050058', '86050083', '86050131', '86050154', '86050004', '86050023', '86050043', '86050059', '86050090', '86050132', '86050155', '86050006', '86050026', '86050044', '86050061', '86050095', '86050138', '86050156', '86050011', '86050027', '86050045', '86050062', '86050097', '86050140', '86050159', '86050012', '86050028', '86050049', '86050065', '86050103', '86050142', '86050160', '86050013', '86050030', '86050050', '86050066', '86050117', '86050143', '86050162', '86050015', '86050032', '86050051', '86050067', '86050119', '86050144', '86050164', '86050019', '86050033', '86050055', '86050068', '86050123', '86050149', '86050165', '86050020', '86050035', '86050056', '86050071', '86050124', '86050150', '86050166', '86050167', '86050184', '86050207', '86050228', '86050251', '86050279', '86050297', '86050168', '86050189', '86050208', '86050230', '86050257', '86050282', '86050298', '86050171', '86050190', '86050210', '86050235', '86050259', '86050283', '86050301', '86050173', '86050192', '86050211', '86050236', '86050260', '86050284', '86050303', '86050174', '86050193', '86050212', '86050243', '86050261', '86050285', '86050304', '86050175', '86050197', '86050218', '86050244', '86050262', '86050289', '86050305', '86050176', '86050202', '86050219', '86050245', '86050267', '86050291', '86050307', '86050177', '86050203', '86050224', '86050246', '86050268', '86050293', '86050309', '86050179', '86050204', '86050225', '86050247', '86050270', '86050295', '86050312', '86050180', '86050205', '86050226', '86050248', '86050274', '86050296', '86050319', '86050320', '86050330', '86050334', '86050338', '86050344', '86050358', '86070135', '86050323', '86050331', '86050336', '86050342', '86050350', '86050360', '86140288', '86050327', '86050333']

Board_6 = ['86060001', '86060039', '86060058', '86060087', '86060150', '86060206', '86060286', '86060002', '86060041', '86060059', '86060103', '86060155', '86060207', '86060287', '86060003', '86060042', '86060061', '86060105', '86060167', '86060218', '86060290', '86060005', '86060044', '86060062', '86060106', '86060176', '86060219', '86060292', '86060012', '86060047', '86060063', '86060107', '86060179', '86060221', '86060293', '86060027', '86060049', '86060065', '86060111', '86060181', '86060229', '86060295', '86060031', '86060050', '86060067', '86060112', '86060187', '86060231', '86060298', '86060032', '86060051', '86060076', '86060123', '86060189', '86060252', '86060301', '86060033', '86060052', '86060079', '86060126', '86060200', '86060262', '86060312', '86060038', '86060054', '86060086', '86060129', '86060204', '86060280', '86060317', '86060321', '86060325', '86060333', '86060336', '86060346', '86060348', '86060352', '86060322', '86060327', '86060335', '86060345']

Board_7 = ['86070003', '86070057', '86070109', '86070156', '86070177', '86070230', '86070245', '86070004', '86070061', '86070111', '86070157', '86070181', '86070232', '86070247', '86070006', '86070070', '86070112', '86070158', '86070187', '86070234', '86070248', '86070010', '86070073', '86070113', '86070161', '86070189', '86070235', '86070250', '86070033', '86070074', '86070115', '86070164', '86070197', '86070238', '86070252', '86070034', '86070075', '86070140', '86070166', '86070201', '86070239', '86070255', '86070035', '86070082', '86070150', '86070169', '86070206', '86070240', '86070260', '86070037', '86070084', '86070151', '86070172', '86070209', '86070241', '86070262', '86070043', '86070088', '86070152', '86070173', '86070224', '86070243', '86070269', '86070055', '86070092', '86070154', '86070174', '86070225', '86070244', '86070270', '86070275', '86070299', '86070305', '86070334', '86070053', '86070103', '86070122', '86070279', '86070300', '86070311', '86070335', '86070086', '86070116', '86070123', '86070280', '86070301', '86070325', '86070340', '86070095', '86070119', '86070138', '86070281', '86070302', '86070332', '86070017', '86070101', '86070121', '86070147', '86070297', '86070303']

Board_8 = ['86080007', '86080040', '86080075', '86080111', '86080192', '86080258', '86080016', '86080029', '86080041', '86080077', '86080125', '86080202', '86080014', '86080018', '86080035', '86080044', '86080081', '86080170', '86080207']

Board_9 = ['86090003', '86090071', '86090104', '86090143', '86090169', '86090206', '86090283', '86090007', '86090074', '86090112', '86090144', '86090174', '86090210', '86090284', '86090009', '86090075', '86090113', '86090150', '86090176', '86090220', '86090303', '86090017', '86090086', '86090123', '86090151', '86090193', '86090237', '86090328', '86090018', '86090095', '86090131', '86090154', '86090196', '86090239', '86170303', '86090032', '86090098', '86090132', '86090155', '86090197', '86090252', '86090275', '86090067', '86090100', '86090134', '86090159', '86090198', '86090280', '86090307']

Board_10 = ['86100005', '86100099', '86100154', '86100203', '86100343', '86100034', '86100267', '86100009', '86100108', '86100158', '86100207', '86100346', '86100040', '86100280', '86100017', '86100109', '86100159', '86100250', '86100354', '86100244', '86100281', '86100026', '86100125', '86100162', '86100251', '86100355', '86100263', '86100283', '86100054', '86100129', '86100168', '86100315', '86100024', '86100265', '86100334', '86100059', '86100134', '86100199', '86100330']

Board_11 = ['86110004', '86110104', '86110153', '86110198', '86110261', '86110322', '86110049', '86110007', '86110107', '86110154', '86110199', '86110264', '86110326', '86110051', '86110015', '86110112', '86110157', '86110212', '86110266', '86110331', '86110053', '86110016', '86110115', '86110162', '86110225', '86110272', '86110018', '86110060', '86110021', '86110116', '86110163', '86110226', '86110281', '86110020', '86110068', '86110022', '86110125', '86110165', '86110227', '86110283', '86110029', '86110070', '86110039', '86110136', '86110166', '86110228', '86110290', '86110033', '86110219', '86110058', '86110137', '86110171', '86110231', '86110305', '86110035', '86110291', '86110059', '86110140', '86110181', '86110234', '86110306', '86110040', '86110292', '86110074', '86110143', '86110184', '86110243', '86110310', '86110044', '86110294', '86110096', '86110146', '86110187', '86110255', '86110321', '86110047', '86110298', '86110097', '86110147', '86110197', '86110259']

Board_12 = ['86120002', '86120070', '86120124', '86120193', '86120225', '86120271', '86120148', '86120012', '86120071', '86120125', '86120198', '86120240', '86120292', '86120156', '86120015', '86120073', '86120130', '86120205', '86120246', '86120297', '86120274', '86120018', '86120077', '86120155', '86120210', '86120247', '86120298', '86120280', '86120026', '86120084', '86120180', '86120214', '86120252', '86120301', '86120283', '86120036', '86120093', '86120185', '86120217', '86120260', '86120326', '86120294', '86120056', '86120108', '86120188', '86120222', '86120265', '86120025', '86120338', '86120065', '86120116', '86120190']

Board_13 = ['86130009', '86130089', '86130133', '86130170', '86130235', '86130293', '86130171', '86130013', '86130092', '86130137', '86130174', '86130237', '86130302', '86130185', '86130016', '86130093', '86130140', '86130182', '86130239', '86130306', '86130197', '86130023', '86130100', '86130144', '86130186', '86130252', '86130309', '86130205', '86130035', '86130101', '86130145', '86130188', '86130257', '86130320', '86130219', '86130037', '86130120', '86130150', '86130189', '86130276', '86130321', '86130248', '86130042', '86130125', '86130157', '86130209', '86130277', '86130325', '86130266', '86130062', '86130126', '86130161', '86130212', '86130281', '86130007', '86130268', '86130070', '86130129', '86130163', '86130213', '86130286', '86130014', '86130273', '86130073', '86130130', '86130166', '86130214', '86130287', '86130054', '86130313', '86130082', '86130132', '86130168', '86130226', '86130288']

Board_14 = ['86140011', '86140097', '86140155', '86140236', '86140301', '86140328', '86140244', '86140045', '86140105', '86140188', '86140240', '86140305', '86140338', '86140270', '86140054', '86140106', '86140190', '86140243', '86140307', '86140339', '86140273', '86140061', '86140125', '86140198', '86140250', '86140310', '86140158', '86140277', '86140069', '86140131', '86140199', '86140254', '86140311', '86140165', '86140283', '86140073', '86140143', '86140202', '86140264', '86140313', '86140172', '86140285', '86140078', '86140146', '86140212', '86140265', '86140314', '86140177', '86140316', '86140081', '86140148', '86140217', '86140298', '86140323', '86140200', '86140317', '86140089', '86140149']

Board_15 = ['86150002', '86150044', '86150079', '86150115', '86150154', '86150204', '86150266', '86150006', '86150045', '86150080', '86150121', '86150161', '86150205', '86150270', '86150009', '86150050', '86150082', '86150123', '86150164', '86150208', '86150294', '86150011', '86150058', '86150087', '86150128', '86150168', '86150210', '86150309', '86150013', '86150059', '86150089', '86150135', '86150170', '86150234', '86150003', '86150018', '86150060', '86150094', '86150138', '86150176', '86150245', '86150029', '86150020', '86150062', '86150095', '86150143', '86150184', '86150249', '86150102', '86150027', '86150066', '86150100', '86150146', '86150191', '86150251', '86150259', '86150028', '86150068', '86150104', '86150148', '86150197', '86150264', '86150260', '86150039', '86150069']

Board_16 = ['86160004', '86160051', '86160107', '86160146', '86160211', '86160297', '86160055', '86160012', '86160059', '86160111', '86160148', '86160212', '86160300', '86160195', '86160015', '86160075', '86160114', '86160158', '86160213', '86160303', '86160209', '86160028', '86160079', '86160117', '86160168', '86160238', '86160308', '86160216', '86160040', '86160080', '86160127', '86160171', '86160249', '86160310', '86160259', '86160045', '86160086', '86160128', '86160176', '86160265', '86160315', '86160261', '86160047', '86160094', '86160132', '86160200', '86160295', '86160317', '86160286', '86160050', '86160104', '86160145', '86160203']

Board_17 = ['86170004', '86170050', '86170093', '86170140', '86170201', '86170259', '86170275', '86170008', '86170058', '86170097', '86170157', '86170209', '86170268', '86170287', '86170010', '86170070', '86170114', '86170162', '86170220', '86170269', '86170099', '86170038', '86170077', '86170131', '86170169', '86170242', '86170272', '86170104', '86170045', '86170092', '86170135', '86170179', '86170246']

Board_18_19 = ['86180002', '86180037', '86180093', '86180129', '86180148', '86180173', '86180218', '86180005', '86180049', '86180098', '86180130', '86180152', '86180182', '86180220', '86180006', '86180054', '86180109', '86180131', '86180154', '86180183', '86180225', '86180007', '86180060', '86180118', '86180133', '86180157', '86180185', '86180230', '86180012', '86180064', '86180120', '86180135', '86180158', '86180193', '86180236', '86180026', '86180067', '86180123', '86180139', '86180161', '86180209', '86180238', '86180030', '86180076', '86180125', '86180142', '86180162', '86180210', '86180239', '86180031', '86180079', '86180126', '86180143', '86180163', '86180211', '86180240', '86180034', '86180080', '86180127', '86180145', '86180166', '86180212', '86180243', '86180036', '86180089', '86180128', '86180146', '86180172', '86180214', '86180245', '86180247', '86180292', '86190015', '86190062', '86190104', '86190156', '86190206', '86180263', '86180295', '86190027', '86190071', '86190108', '86190164', '86190217', '86180270', '86180301', '86190029', '86190075', '86190112', '86190166', '86190224', '86180273', '86180304', '86190031', '86190077', '86190129', '86190169', '86190231', '86180274', '86180305', '86190039', '86190086', '86190130', '86190174', '86190239', '86180275', '86180317', '86190040', '86190091', '86190131', '86190177', '86190258', '86180281', '86180318', '86190044', '86190094', '86190132', '86190180', '86190263', '86180283', '86190001', '86190051', '86190098', '86190133', '86190197', '86190264', '86180286', '86190010', '86190055', '86190101', '86190140', '86190202', '86190265', '86180291', '86190012', '86190061', '86190102', '86190143', '86190203', '86190286', '86190290', '86180008', '86180208', '86180254', '86180259', '86180287', '86190036', '86190292', '86180055', '86180252', '86180257', '86180261', '86180310', '86190087', '86190299', '86180200', '86180253', '86180258', '86180279', '86190002', '86190187', '86190305', '86180201']

#create how many candidates have left from each board to issb and set to variable
left_1 = len(list(set(final_list).intersection(set(Board_1))))
left_2 = len(list(set(final_list).intersection(set(Board_2))))
left_3 = len(list(set(final_list).intersection(set(Board_3))))
left_4 = len(list(set(final_list).intersection(set(Board_4))))
left_5 = len(list(set(final_list).intersection(set(Board_5))))
left_6 = len(list(set(final_list).intersection(set(Board_6))))
left_7 = len(list(set(final_list).intersection(set(Board_7))))
left_8 = len(list(set(final_list).intersection(set(Board_8))))
left_9 = len(list(set(final_list).intersection(set(Board_9))))
left_10 = len(list(set(final_list).intersection(set(Board_10))))
left_11 = len(list(set(final_list).intersection(set(Board_11))))
left_12 = len(list(set(final_list).intersection(set(Board_12))))
left_13 = len(list(set(final_list).intersection(set(Board_13))))
left_14 = len(list(set(final_list).intersection(set(Board_14))))
left_15 = len(list(set(final_list).intersection(set(Board_15))))
left_16 = len(list(set(final_list).intersection(set(Board_16))))
left_17 = len(list(set(final_list).intersection(set(Board_17))))
left_18_19 = len(list(set(final_list).intersection(set(Board_18_19))))

def breaker():
	print("\n")

breaker()

#merge all boards and calculate cadet colleges and how many are left
total_written_passed = (Board_1) + (Board_2) + (Board_3) + (Board_4) + (Board_5) + (Board_6) + (Board_7) + (Board_8) + (Board_9) + (Board_10) + (Board_11) + (Board_12) + (Board_13) + (Board_14) + (Board_15) + (Board_16) + (Board_17) + (Board_18_19)

writtened_issb = len(list(set(total_written_passed).intersection(set(final_list))))

print(f"**Total {len(total_written_passed)} candidates have passed the written exam. ")
print(f"**{(writtened_issb)} out of them have been called for issb. ")
breaker()
#print(left_1, left_2, left_3, left_4, left_5, left_6, left_7, left_8, left_9, left_10, left_11, left_12, left_13, left_14, left_15, left_16, left_17, left_18_19)

print(f"-From Board-1: Cantt Girls' Public School & College, Dhaka Cantt {'.'*10} out of {len(Board_1)} candidates {'.'*5} {left_1} have been called to issb.")

print(f"-From Board-2: Shaheed Romiz uddin Cantt College, Dhaka Cantt {'.'*10} out of {len(Board_2)} candidates {'.'*5} {left_2} have been called to issb.")

print(f"-From Board-3: Mirpur Cantt Public School & College, Mirpur Cantt {'.'*10} out of {len(Board_3)} candidates {'.'*5} {left_3} have been called to issb.")

print(f"-From Board-4: Mirpur Cantt Public School & College, Mirpur Cantt {'.'*10} out of {len(Board_4)} candidates {'.'*5} {left_4} have been called to issb.")

print(f"-From Board-5: Cantt Girls' Public School & College, Dhaka Cantt {'.'*10} out of {len(Board_5)} candidates {'.'*5} {left_5} have been called to issb.")

print(f"-From Board-6: Adamjee Cantt Public School, Dhaka Cantt {'.'*10} out of {len(Board_6)} candidates {'.'*5} {left_6} have been called to issb.")

print(f"-From Board-7: Cantt Public School & College, Savar Cantt {'.'*10} out of {len(Board_7)} candidates {'.'*5} {left_7} have been called to issb.")

print(f"-From Board-8: Cantt Public School & College, Ramu Cantt {'.'*10} out of {len(Board_8)} candidates {'.'*5} {left_8} have been called to issb.")

print(f"-From Board-9: Cantt Board High School, Bogura Cantt {'.'*10} out of {len(Board_9)} candidates {'.'*5} {left_9} have been called to issb.")

print(f"-From Board-10: Cantt Board High School, Rajshahi Cantt {'.'*10} out of {len(Board_10)} candidates {'.'*5} {left_10} have been called to issb.")

print(f"-From Board-11: Cantt Public School & College, Shaheed Salahuddin Cantt {'.'*10} out of {len(Board_11)} candidates {'.'*5} {left_11} have been called to issb.")

print(f"-From Board-12: Cantt Board High School, Momenshahi Cantt {'.'*10} out of {len(Board_12)} candidates {'.'*5} {left_12} have been called to issb.")

print(f"-From Board-13: Cantt Public School & College Chattogram Cantt {'.'*10} out of {len(Board_13)} candidates {'.'*5} {left_13} have been called to issb.")

print(f"-From Board-14: Ispahani Public School & College, Cumilla Cantt {'.'*10} out of {len(Board_14)} candidates {'.'*5} {left_14} have been called to issb.")

print(f"-From Board-15: Cantt Board High school, Jalalabad Cantt {'.'*10} out of {len(Board_15)} candidates {'.'*5} {left_15} have been called to issb.")

print(f"-From Board-16: Cantt Collage, Jashore Cantt {'.'*10} out of {len(Board_16)} candidates {'.'*5} {left_16} have been called to issb.")

print(f"-From Board-17: Cantt Public School & College, Jahanabad Cantt, Khulna {'.'*10} out of {len(Board_17)} candidates {'.'*5} {left_17} have been called to issb.")

print(f"-From Board-18 & 19: Cantt Public School & College, Rangpur Cantt {'.'*10} out of {len(Board_18_19)} candidates {'.'*5} {left_18_19} have been called to issb.")

breaker()

print(f"#{len(final_list) - writtened_issb} Have been called to issb from Cadet colleges & MCSK.")
breaker()
print(f"#Total {len(final_list)} candidates have been called to issb. ")
breaker()
print(f"#{len(total_written_passed) - (writtened_issb)} candidates are left to call for issb.(This dosen\'t include Cadet colleges). ")
breaker()
breaker()
