# This file will build the necessary numpy arrays for the model
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'batches')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'imports')))
from models.sud.data.batches.__pull_batches import get_training_data
training_data = get_training_data()

# Data for NOBL____________________________________________________________________________
def nobl_fu(training_data):
	nobl = training_data['nobl']
	nobl_1 = nobl[0].to_numpy()
	nobl_2 = nobl[1].to_numpy()
	nobl_3 = nobl[2].to_numpy()
	nobl_4 = nobl[3].to_numpy()
	nobl_5 = nobl[4].to_numpy()
	return [nobl_1, nobl_2, nobl_3, nobl_4, nobl_5]

# Data for VYMI ____________________________________________________________________________
def vymi_fu(training_data):
	vymi = training_data['vymi']
	vymi_1 = vymi[0].to_numpy()
	vymi_2 = vymi[1].to_numpy()
	vymi_3 = vymi[2].to_numpy()
	vymi_4 = vymi[3].to_numpy()
	vymi_5 = vymi[4].to_numpy()
	return [vymi_1, vymi_2, vymi_3, vymi_4, vymi_5]

# Data for PEY ____________________________________________________________________________
def pey_fu(training_data):
	pey = training_data['pey']
	pey_1 = pey[0].to_numpy()
	pey_2 = pey[1].to_numpy()
	pey_3 = pey[2].to_numpy()
	pey_4 = pey[3].to_numpy()
	pey_5 = pey[4].to_numpy()
	return [pey_1, pey_2, pey_3, pey_4, pey_5]

# Data for XLE ____________________________________________________________________________
def xle_fu(training_data):
	xle = training_data['xle']
	xle_1 = xle[0].to_numpy()
	xle_2 = xle[1].to_numpy()
	xle_3 = xle[2].to_numpy()
	xle_4 = xle[3].to_numpy()
	xle_5 = xle[4].to_numpy()
	return [xle_1, xle_2, xle_3, xle_4, xle_5]

# Data for VYM ____________________________________________________________________________
def vym_fu(training_data):
	vym = training_data['vym']
	vym_1 = vym[0].to_numpy()
	vym_2 = vym[1].to_numpy()
	vym_3 = vym[2].to_numpy()
	vym_4 = vym[3].to_numpy()
	vym_5 = vym[4].to_numpy()
	return [vym_1, vym_2, vym_3, vym_4, vym_5]

# Data for HDV ____________________________________________________________________________
def hdv_fu(training_data):
	hdv = training_data['hdv']
	hdv_1 = hdv[0].to_numpy()
	hdv_2 = hdv[1].to_numpy()
	hdv_3 = hdv[2].to_numpy()
	hdv_4 = hdv[3].to_numpy()
	hdv_5 = hdv[4].to_numpy()
	return [hdv_1, hdv_2, hdv_3, hdv_4, hdv_5]

# Data for GLNCY ____________________________________________________________________________
def glncy_fu(training_data):
	glncy = training_data['glncy']
	glncy_1 = glncy[0].to_numpy()
	glncy_2 = glncy[1].to_numpy()
	glncy_3 = glncy[2].to_numpy()
	glncy_4 = glncy[3].to_numpy()
	glncy_5 = glncy[4].to_numpy()
	return [glncy_1, glncy_2, glncy_3, glncy_4, glncy_5]

# Data for DGRO ____________________________________________________________________________
def dgro_fu(training_data):
	dgro = training_data['dgro']
	dgro_1 = dgro[0].to_numpy()
	dgro_2 = dgro[1].to_numpy()
	dgro_3 = dgro[2].to_numpy()
	dgro_4 = dgro[3].to_numpy()
	dgro_5 = dgro[4].to_numpy()
	return [dgro_1, dgro_2, dgro_3, dgro_4, dgro_5]

# Data for VB ____________________________________________________________________________
def vb_fu(training_data):
	vb = training_data['vb']
	vb_1 = vb[0].to_numpy()
	vb_2 = vb[1].to_numpy()
	vb_3 = vb[2].to_numpy()
	vb_4 = vb[3].to_numpy()
	vb_5 = vb[4].to_numpy()
	return [vb_1, vb_2, vb_3, vb_4, vb_5]

# Data for JNK ____________________________________________________________________________
def jnk_fu(training_data):
	jnk = training_data['jnk']
	jnk_1 = jnk[0].to_numpy()
	jnk_2 = jnk[1].to_numpy()
	jnk_3 = jnk[2].to_numpy()
	jnk_4 = jnk[3].to_numpy()
	jnk_5 = jnk[4].to_numpy()
	return [jnk_1, jnk_2, jnk_3, jnk_4, jnk_5]

# Data for HYG ____________________________________________________________________________
def hyg_fu(training_data):
	hyg = training_data['hyg']
	hyg_1 = hyg[0].to_numpy()
	hyg_2 = hyg[1].to_numpy()
	hyg_3 = hyg[2].to_numpy()
	hyg_4 = hyg[3].to_numpy()
	hyg_5 = hyg[4].to_numpy()
	return [hyg_1, hyg_2, hyg_3, hyg_4, hyg_5]

# Data for SCHD ____________________________________________________________________________
def schd_fu(training_data):
	schd = training_data['schd']
	schd_1 = schd[0].to_numpy()
	schd_2 = schd[1].to_numpy()
	schd_3 = schd[2].to_numpy()
	schd_4 = schd[3].to_numpy()
	schd_5 = schd[4].to_numpy()
	return [schd_1, schd_2, schd_3, schd_4, schd_5]

# Data for IXUS ____________________________________________________________________________
def ixus_fu(training_data):
	ixus = training_data['ixus']
	ixus_1 = ixus[0].to_numpy()
	ixus_2 = ixus[1].to_numpy()
	ixus_3 = ixus[2].to_numpy()
	ixus_4 = ixus[3].to_numpy()
	ixus_5 = ixus[4].to_numpy()
	return [ixus_1, ixus_2, ixus_3, ixus_4, ixus_5]

# Data for DJIA ____________________________________________________________________________
def djia_fu(training_data):
	djia = training_data['djia']
	djia_1 = djia[0].to_numpy()
	djia_2 = djia[1].to_numpy()
	djia_3 = djia[2].to_numpy()
	djia_4 = djia[3].to_numpy()
	djia_5 = djia[4].to_numpy()
	return [djia_1, djia_2, djia_3, djia_4, djia_5]

# Data for LIT ____________________________________________________________________________
def lit_fu(training_data):
	lit = training_data['lit']
	lit_1 = lit[0].to_numpy()
	lit_2 = lit[1].to_numpy()
	lit_3 = lit[2].to_numpy()
	lit_4 = lit[3].to_numpy()
	lit_5 = lit[4].to_numpy()
	return [lit_1, lit_2, lit_3, lit_4, lit_5]

# Data for SPHD ____________________________________________________________________________
def sphd_fu(training_data):
	sphd = training_data['sphd']
	sphd_1 = sphd[0].to_numpy()
	sphd_2 = sphd[1].to_numpy()
	sphd_3 = sphd[2].to_numpy()
	sphd_4 = sphd[3].to_numpy()
	sphd_5 = sphd[4].to_numpy()
	return [sphd_1, sphd_2, sphd_3, sphd_4, sphd_5]

# Data for ISCF ____________________________________________________________________________
def iscf_fu(training_data):
	iscf = training_data['iscf']
	iscf_1 = iscf[0].to_numpy()
	iscf_2 = iscf[1].to_numpy()
	iscf_3 = iscf[2].to_numpy()
	iscf_4 = iscf[3].to_numpy()
	iscf_5 = iscf[4].to_numpy()
	return [iscf_1, iscf_2, iscf_3, iscf_4, iscf_5]

# Data for HSCZ ____________________________________________________________________________
def hscz_fu(training_data):
	hscz = training_data['hscz']
	hscz_1 = hscz[0].to_numpy()
	hscz_2 = hscz[1].to_numpy()
	hscz_3 = hscz[2].to_numpy()
	hscz_4 = hscz[3].to_numpy()
	hscz_5 = hscz[4].to_numpy()
	return [hscz_1, hscz_2, hscz_3, hscz_4, hscz_5]

# Data for HDEF ____________________________________________________________________________
def hdef_fu(training_data):
	hdef = training_data['hdef']
	hdef_1 = hdef[0].to_numpy()
	hdef_2 = hdef[1].to_numpy()
	hdef_3 = hdef[2].to_numpy()
	hdef_4 = hdef[3].to_numpy()
	hdef_5 = hdef[4].to_numpy()
	return [hdef_1, hdef_2, hdef_3, hdef_4, hdef_5]

# Data for PCY ____________________________________________________________________________
def pcy_fu(training_data):
	pcy = training_data['pcy']
	pcy_1 = pcy[0].to_numpy()
	pcy_2 = pcy[1].to_numpy()
	pcy_3 = pcy[2].to_numpy()
	pcy_4 = pcy[3].to_numpy()
	pcy_5 = pcy[4].to_numpy()
	return [pcy_1, pcy_2, pcy_3, pcy_4, pcy_5]

# Data for BNDX ____________________________________________________________________________
def bndx_fu(training_data):
	bndx = training_data['bndx']
	bndx_1 = bndx[0].to_numpy()
	bndx_2 = bndx[1].to_numpy()
	bndx_3 = bndx[2].to_numpy()
	bndx_4 = bndx[3].to_numpy()
	bndx_5 = bndx[4].to_numpy()
	return [bndx_1, bndx_2, bndx_3, bndx_4, bndx_5]

# Data for SMX ____________________________________________________________________________
def smx_fu(training_data):
	smx = training_data['smx']
	smx_1 = smx[0].to_numpy()
	smx_2 = smx[1].to_numpy()
	smx_3 = smx[2].to_numpy()
	smx_4 = smx[3].to_numpy()
	smx_5 = smx[4].to_numpy()
	return [smx_1, smx_2, smx_3, smx_4, smx_5]

# Data for HEFA ____________________________________________________________________________
def hefa_fu(training_data):
	hefa = training_data['hefa']
	hefa_1 = hefa[0].to_numpy()
	hefa_2 = hefa[1].to_numpy()
	hefa_3 = hefa[2].to_numpy()
	hefa_4 = hefa[3].to_numpy()
	hefa_5 = hefa[4].to_numpy()
	return [hefa_1, hefa_2, hefa_3, hefa_4, hefa_5]

# Data for IYK ____________________________________________________________________________
def iyk_fu(training_data):
	iyk = training_data['iyk']
	iyk_1 = iyk[0].to_numpy()
	iyk_2 = iyk[1].to_numpy()
	iyk_3 = iyk[2].to_numpy()
	iyk_4 = iyk[3].to_numpy()
	iyk_5 = iyk[4].to_numpy()
	return [iyk_1, iyk_2, iyk_3, iyk_4, iyk_5]

# Data for USOI ____________________________________________________________________________
def usoi_fu(training_data):
	usoi = training_data['usoi']
	usoi_1 = usoi[0].to_numpy()
	usoi_2 = usoi[1].to_numpy()
	usoi_3 = usoi[2].to_numpy()
	usoi_4 = usoi[3].to_numpy()
	usoi_5 = usoi[4].to_numpy()
	return [usoi_1, usoi_2, usoi_3, usoi_4, usoi_5]

# Data for XLF ____________________________________________________________________________
def xlf_fu(training_data):
	xlf = training_data['xlf']
	xlf_1 = xlf[0].to_numpy()
	xlf_2 = xlf[1].to_numpy()
	xlf_3 = xlf[2].to_numpy()
	xlf_4 = xlf[3].to_numpy()
	xlf_5 = xlf[4].to_numpy()
	return [xlf_1, xlf_2, xlf_3, xlf_4, xlf_5]

# Data for VFH ____________________________________________________________________________
def vfh_fu(training_data):
	vfh = training_data['vfh']
	vfh_1 = vfh[0].to_numpy()
	vfh_2 = vfh[1].to_numpy()
	vfh_3 = vfh[2].to_numpy()
	vfh_4 = vfh[3].to_numpy()
	vfh_5 = vfh[4].to_numpy()
	return [vfh_1, vfh_2, vfh_3, vfh_4, vfh_5]

# Data for KRE ____________________________________________________________________________
def kre_fu(training_data):
	kre = training_data['kre']
	kre_1 = kre[0].to_numpy()
	kre_2 = kre[1].to_numpy()
	kre_3 = kre[2].to_numpy()
	kre_4 = kre[3].to_numpy()
	kre_5 = kre[4].to_numpy()
	return [kre_1, kre_2, kre_3, kre_4, kre_5]

# Data for IYF ____________________________________________________________________________
def iyf_fu(training_data):
	iyf = training_data['iyf']
	iyf_1 = iyf[0].to_numpy()
	iyf_2 = iyf[1].to_numpy()
	iyf_3 = iyf[2].to_numpy()
	iyf_4 = iyf[3].to_numpy()
	iyf_5 = iyf[4].to_numpy()
	return [iyf_1, iyf_2, iyf_3, iyf_4, iyf_5]

# Data for FNCL ____________________________________________________________________________
def fncl_fu(training_data):
	fncl = training_data['fncl']
	fncl_1 = fncl[0].to_numpy()
	fncl_2 = fncl[1].to_numpy()
	fncl_3 = fncl[2].to_numpy()
	fncl_4 = fncl[3].to_numpy()
	fncl_5 = fncl[4].to_numpy()
	return [fncl_1, fncl_2, fncl_3, fncl_4, fncl_5]

# Data for QQQ ____________________________________________________________________________
def qqq_fu(training_data):
	qqq = training_data['qqq']
	qqq_1 = qqq[0].to_numpy()
	qqq_2 = qqq[1].to_numpy()
	qqq_3 = qqq[2].to_numpy()
	qqq_4 = qqq[3].to_numpy()
	qqq_5 = qqq[4].to_numpy()
	return [qqq_1, qqq_2, qqq_3, qqq_4, qqq_5]

# Data for SPY ____________________________________________________________________________
def spy_fu(training_data):
	spy = training_data['spy']
	spy_1 = spy[0].to_numpy()
	spy_2 = spy[1].to_numpy()
	spy_3 = spy[2].to_numpy()
	spy_4 = spy[3].to_numpy()
	spy_5 = spy[4].to_numpy()
	return [spy_1, spy_2, spy_3, spy_4, spy_5]

# Data for VTI ____________________________________________________________________________
def vti_fu(training_data):
	vti = training_data['vti']
	vti_1 = vti[0].to_numpy()
	vti_2 = vti[1].to_numpy()
	vti_3 = vti[2].to_numpy()
	vti_4 = vti[3].to_numpy()
	vti_5 = vti[4].to_numpy()
	return [vti_1, vti_2, vti_3, vti_4, vti_5]

# Data for ITOT ____________________________________________________________________________
def itot_fu(training_data):
	itot = training_data['itot']
	itot_1 = itot[0].to_numpy()
	itot_2 = itot[1].to_numpy()
	itot_3 = itot[2].to_numpy()
	itot_4 = itot[3].to_numpy()
	itot_5 = itot[4].to_numpy()
	return [itot_1, itot_2, itot_3, itot_4, itot_5]

# Data for XLK ____________________________________________________________________________
def xlk_fu(training_data):
	xlk = training_data['xlk']
	xlk_1 = xlk[0].to_numpy()
	xlk_2 = xlk[1].to_numpy()
	xlk_3 = xlk[2].to_numpy()
	xlk_4 = xlk[3].to_numpy()
	xlk_5 = xlk[4].to_numpy()
	return [xlk_1, xlk_2, xlk_3, xlk_4, xlk_5]

# Data for XLY ____________________________________________________________________________
def xly_fu(training_data):
	xly = training_data['xly']
	xly_1 = xly[0].to_numpy()
	xly_2 = xly[1].to_numpy()
	xly_3 = xly[2].to_numpy()
	xly_4 = xly[3].to_numpy()
	xly_5 = xly[4].to_numpy()
	return [xly_1, xly_2, xly_3, xly_4, xly_5]

# Data for XLV ____________________________________________________________________________
def xlv_fu(training_data):
	xlv = training_data['xlv']
	xlv_1 = xlv[0].to_numpy()
	xlv_2 = xlv[1].to_numpy()
	xlv_3 = xlv[2].to_numpy()
	xlv_4 = xlv[3].to_numpy()
	xlv_5 = xlv[4].to_numpy()
	return [xlv_1, xlv_2, xlv_3, xlv_4, xlv_5]

# Data for EEM ____________________________________________________________________________
def eem_fu(training_data):
	eem = training_data['eem']
	eem_1 = eem[0].to_numpy()
	eem_2 = eem[1].to_numpy()
	eem_3 = eem[2].to_numpy()
	eem_4 = eem[3].to_numpy()
	eem_5 = eem[4].to_numpy()
	return [eem_1, eem_2, eem_3, eem_4, eem_5]

# Data for VEU ____________________________________________________________________________
def veu_fu(training_data):
	veu = training_data['veu']
	veu_1 = veu[0].to_numpy()
	veu_2 = veu[1].to_numpy()
	veu_3 = veu[2].to_numpy()
	veu_4 = veu[3].to_numpy()
	veu_5 = veu[4].to_numpy()
	return [veu_1, veu_2, veu_3, veu_4, veu_5]
