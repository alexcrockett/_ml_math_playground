# Make all the necessary imports
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'batches')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'imports')))
from experiments.sud.tanh_training.batches.__training_data import training_data
from experiments.sud.tanh_training.batches.__training_data import (nobl_fu, vymi_fu, pey_fu, xle_fu, vym_fu,
																   hdv_fu, glncy_fu, dgro_fu, vb_fu, jnk_fu,
																   hyg_fu, schd_fu, ixus_fu, djia_fu, lit_fu,
																   sphd_fu, iscf_fu, hscz_fu, hdef_fu, pcy_fu,
																   bndx_fu, smx_fu, hefa_fu, iyk_fu, usoi_fu,
																   xlf_fu, vfh_fu, kre_fu, iyf_fu, fncl_fu,
																   qqq_fu, spy_fu, vti_fu, itot_fu, xlk_fu,
																   xly_fu, xlv_fu, eem_fu, veu_fu)


nobl_dat = nobl_fu(training_data)
print(nobl_dat)
nobl1 = nobl_dat[0]

