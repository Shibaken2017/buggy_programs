import os


def load_id(fname):
  ouput_list=[]
  with open(fname,"r")as reader:
    for line in reader:
      tmp=line.strip().split("\t")
      ouput_list.append(tmp[0])

  return ouput_list


def check_file_line(fname):
  '''
  行数数える
  :param fname:
  :return:
  '''
  follow=0
  follolwer=0
  with open(fname,"r")as reader:
    for line in reader:
      if line.startswith("follow\t"):
        follow+=1
      elif line.startswith("follower\t"):
        follolwer+=1


  return follow,follolwer











if __name__=="__main__":

  tmp=load_id("id.txt")
 # with open("check.tsv","w")as writer:
  #  writer.write("id\tfollow\tfollower\n")
   # for id in tmp:
    #  follow,follower=check_file_line(os.path.join("tsv_files","20180706_132352",id+".tsv"))
     # writer.write("{}\t{}\t{}\n".format(id,follow,follower))
  fname="541744"
  fname2="132048"
  print(check_file_line(os.path.join("data_tmp",fname+".tsv")))
  print(check_file_line(os.path.join("data_tmp",fname2+".tsv")))



