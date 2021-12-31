dataset = 'test'
ihdp_1_100_x_setting_b = np.zeros((224,25,100))
ihdp_1_100_t_setting_b = np.zeros((224,100))
ihdp_1_100_yf_setting_b = np.zeros((224,100))
ihdp_1_100_ycf_setting_b = np.zeros((224,100))
ihdp_1_100_mu0_setting_b = np.zeros((224,100))
ihdp_1_100_mu1_setting_b = np.zeros((224,100))
for i in range(100):
  file_path = '/content/ihdp_setting_b/ihdp_npci_{}_{}.csv'.format(dataset,i+1)
  ihdp_file = pd.read_csv(file_path)
  ihdp_1_100_x_setting_b[:,:,i] = ihdp_file.iloc[:,5:].values
  ihdp_1_100_t_setting_b[:,i] = ihdp_file['treatment'].values
  ihdp_1_100_yf_setting_b[:,i] = ihdp_file['y_factual'].values
  ihdp_1_100_ycf_setting_b[:,i] = ihdp_file['y_cfactual'].values
  ihdp_1_100_mu0_setting_b[:,i] = ihdp_file['mu0'].values
  ihdp_1_100_mu1_setting_b[:,i] = ihdp_file['mu1'].values

np.savez('ihdp_setting_b_1-100.test',
         x=ihdp_1_100_x_setting_b,
         t=ihdp_1_100_t_setting_b,
         yf=ihdp_1_100_yf_setting_b,
         ycf=ihdp_1_100_ycf_setting_b,
         mu0=ihdp_1_100_mu0_setting_b,
         mu1=ihdp_1_100_mu1_setting_b)