# This file aggregates all the data into a dictionary for reuse elsewhere

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the necessary module from the parent directory
import _01_sud_noble_batches as train1
import _02_sud_vymi_batches as train2
import _03_sud_pey_batches as train3
import _04_sud_xle_batches as train4
import _05_sud_vym_batches as train5
import _06_sud_hdv_batches as train6
import _07_sud_glncy_batches as train7
import _08_sud_dgro_batches as train8
import _09_sud_vb_batches as train9
import _10_sud_jnk_batches as train10
import _11_sud_hyg_batches as train11
import _12_sud_schd_batches as train12
import _13_sud_ixus_batches as train13
import _14_sud_djia_batches as train14
import _15_sud_lit_batches as train15
import _16_sud_sphd_batches as train16
import _17_sud_iscf_batches as train17
import _18_sud_hscz_batches as train18
import _19_sud_hdef_batches as train19
import _20_sud_pcy_batches as train20
import _21_sud_bndx_batches as train21
import _22_sud_smx_batches as train22
import _23_sud_hefa_batches as train23
import _24_sud_iyk_batches as train24
import _25_sud_usoi_batches as train25
import _26_sud_xlf_batches as train26
import _27_sud_vfh_batches as train27
import _28_sud_kre_batches as train28
import _29_sud_iyf_batches as train29
import _30_sud_fncl_batches as train30
import _31_sud_qqq_batches as train31
import _32_sud_spy_batches as train32
import _33_sud_vti_batches as train33
import _34_sud_itot_batches as train34
import _35_sud_xlk_batches as train35
import  _36_sud_xly_batches as train36
import  _37_sud_xlv_batches as train37
import  _38_sud_eem_batches as train38
import  _39_sud_veu_batches as train39

def get_training_data():
	training_data = {
		'nobl': train1, 'vymi': train2, 'pey': train3, 'xle': train4, 'vym': train5,
		'hdv': train6, 'glncy': train7, 'dgro': train8, 'vb': train9, 'jnk': train10,
		'hyg': train11, 'schd': train12, 'ixus': train13, 'djia': train14, 'lit': train15,
		'sphd': train16, 'iscf': train17, 'hscz': train18, 'hdef': train19, 'pcy': train20,
		'bndx': train21, 'smx': train22, 'hefa': train23, 'iyk': train24, 'usoi': train25,
		'xlf': train26, 'vfh': train27, 'kre': train28, 'iyf': train29, 'fncl': train30,
		'qqq': train31, 'spy': train32, 'vti': train33, 'itot': train34, 'xlk': train35,
		'xly': train36, 'xlv': train37, 'eem': train38, 'veu': train39
	}
	return training_data

def main():
	training_data = get_training_data()
	return training_data

if __name__ == "__main__":
	main()
