# conda create -n sparktts -y python=3.12
# To activate this environment, use                                                                                                                                       
#                                                                                                                                                                         
#     $ conda activate sparktts                                                                                                                                           
#
# To deactivate an active environment, use
#
#     $ conda deactivate

export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890

python download-model.py