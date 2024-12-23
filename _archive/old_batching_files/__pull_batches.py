# This file aggregates all the data into a dictionary for reuse elsewhere

import os
import sys

# Add the parent directory (sud) to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Verify paths (optional step for debugging)
print(sys.path)

# Import the necessary modules
import _01_sud_noble_batches as train1
from sud.sud._archive.old_batching_files import _37_sud_xlv_batches as train37, _13_sud_ixus_batches as train13, \
	_16_sud_sphd_batches as train16, _35_sud_xlk_batches as train35, _18_sud_hscz_batches as train18, \
	_03_sud_pey_batches as train3, _17_sud_iscf_batches as train17, _06_sud_hdv_batches as train6, \
	_31_sud_qqq_batches as train31, _21_sud_bndx_batches as train21, _30_sud_fncl_batches as train30, \
	_02_sud_vymi_batches as train2, _14_sud_djia_batches as train14, _08_sud_dgro_batches as train8, \
	_10_sud_jnk_batches as train10, _19_sud_hdef_batches as train19, _07_sud_glncy_batches as train7, \
	_22_sud_smx_batches as train22, _38_sud_eem_batches as train38, _29_sud_iyf_batches as train29, \
	_12_sud_schd_batches as train12, _33_sud_vti_batches as train33, _32_sud_spy_batches as train32, \
	_05_sud_vym_batches as train5, _15_sud_lit_batches as train15, _39_sud_veu_batches as train39, \
	_11_sud_hyg_batches as train11, _25_sud_usoi_batches as train25, _24_sud_iyk_batches as train24, \
	_27_sud_vfh_batches as train27, _36_sud_xly_batches as train36, _04_sud_xle_batches as train4, \
	_09_sud_vb_batches as train9, _26_sud_xlf_batches as train26, _28_sud_kre_batches as train28, \
	_34_sud_itot_batches as train34, _20_sud_pcy_batches as train20, _23_sud_hefa_batches as train23

nob_list = train1.main()
vymi_list = train2.main()
pey_list = train3.main()
xle_list = train4.main()
vym_list = train5.main()
hdv_list = train6.main()
glncy_list = train7.main()
dgro_list = train8.main()
vb_list = train9.main()
jnk_list = train10.main()
hyg_list = train11.main()
schd_list = train12.main()
ixus_list = train13.main()
djia_list = train14.main()
lit_list = train15.main()
sphd_list = train16.main()
iscf_list = train17.main()
hscz_list = train18.main()
hdef_list = train19.main()
pcy_list = train20.main()
bndx_list = train21.main()
smx_list = train22.main()
hefa_list = train23.main()
iyk_list = train24.main()
usoi_list = train25.main()
xlf_list = train26.main()
vfh_list = train27.main()
kre_list = train28.main()
iyf_list = train29.main()
fncl_list = train30.main()
qqq_list = train31.main()
spy_list = train32.main()
vti_list = train33.main()
itot_list = train34.main()
xlk_list = train35.main()
xly_list = train36.main()
xlv_list = train37.main()
eem_list = train38.main()
veu_list = train39.main()

def get_training_data():
	training_data = {
		'nobl': nob_list, 'vymi': vymi_list, 'pey': pey_list, 'xle': xle_list, 'vym': vym_list,
		'hdv': hdv_list, 'glncy': glncy_list, 'dgro': dgro_list, 'vb': vb_list, 'jnk': jnk_list,
		'hyg': hyg_list, 'schd': schd_list, 'ixus': ixus_list, 'djia': djia_list, 'lit': lit_list,
		'sphd': sphd_list, 'iscf': iscf_list, 'hscz': hscz_list, 'hdef': hdef_list, 'pcy': pcy_list,
		'bndx': bndx_list, 'smx': smx_list, 'hefa': hefa_list, 'iyk': iyk_list, 'usoi': usoi_list,
		'xlf': xlf_list, 'vfh': vfh_list, 'kre': kre_list, 'iyf': iyf_list, 'fncl': fncl_list,
		'qqq': qqq_list, 'spy': spy_list, 'vti': vti_list, 'itot': itot_list, 'xlk': xlk_list,
		'xly': xly_list, 'xlv': xlv_list, 'eem': eem_list, 'veu': veu_list
	}
	return training_data

def main():
	training_data = get_training_data()
	print(training_data)
	return training_data

if __name__ == "__main__":
	main()
