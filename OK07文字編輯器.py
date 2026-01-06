def main():
    M,N=map(int,input().split())
    Sentence=[]
    for i in range(M):
        Sentence.append(input().split())
    for l in range(N):
        line=input().split()
        cmd=line[0]
        if(cmd=="awf"):
            i=int(line[1])-1
            n=int(line[2])-1
            word=line[3]
            Sentence[i].insert(n,word)
            
        elif(cmd=="awa"):
            i=int(line[1])-1
            n=int(line[2])
            word=line[3]
            Sentence[i].insert(n,word)

        elif(cmd=="asf"):
            i = int(line[1]) - 1
            sentence = line[2:]   
            Sentence[i] = sentence + Sentence[i] 
            
        elif(cmd=="asa"):
            i = int(line[1]) -1
            sentence = line[2:]   
            Sentence[i] = Sentence[i] + sentence
        elif(cmd=="if"):
           key=line[1]
           word=line[2]
           for idx in range(len(Sentence)):
                new_line = []
                for w in Sentence[idx]:
                    if w == key:
                        new_line.append(word)
                    new_line.append(w)
                Sentence[idx] = new_line
        elif cmd == "ia":
            key = line[1]
            word = line[2]
            for idx in range(len(Sentence)):
                new_line = []
                for w in Sentence[idx]:
                    new_line.append(w)
                    if w == key:
                        new_line.append(word)
                Sentence[idx] = new_line
        elif(cmd=="dw"):
            i=int(line[1])-1
            n=int(line[2])-1
            del(Sentence[i][n])
        elif(cmd=="dl"):
            i=int(line[1])-1
            del(Sentence[i])
        elif(cmd=="rp"):
            old=line[1]
            new=line[2]
            for i in range(len(Sentence)):
                for j in range(len(Sentence[i])):
                    if Sentence[i][j] == old:
                        Sentence[i][j] = new
        elif(cmd=="c"):
            count = 0
            for line in Sentence:
                count += len(line)
            print(count)
    for i in Sentence:
        print(" ".join(i))
main()