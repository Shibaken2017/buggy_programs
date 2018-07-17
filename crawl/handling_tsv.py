import os



def write_tsv(fname, id,name, title, follow, follower, type="フォロワー"):
  print(name)
  if not os.path.exists(fname):
    with open(fname, "a")as writer:
      writer.write("フォロー/フォロワー\tid\t名前\t肩書き\tフォロー数\tフォロワー数\n")
      writer.write("{}\t{}\t{}\t{}\t{}\n".format(type,id, name, title, follow, follower))
  else:
    with open(fname, "a")as writer:
      writer.write("{}\t{}\t{}\t{}\t{}\t{}\n".format(type,id,name, title, follow, follower))



def load_id_files(fname):
  output_list=[]
  with open(fname,"r")as reader:

    for line in reader:
      tmp=line.strip().split("\t")[0]
      output_list.append(tmp)
  return output_list

if __name__=="__main__":
  print(load_id_files("id.txt"))
