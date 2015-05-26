// this script is used in Jenkins to display a version list sorted

def oem = "wave_pict"
def droplist = []
def rpath = '\\\\shastorage01\\Share\\Intraoral_Camera_SW_FW_build\\Software_build\\Common'
def mylist=new File(rpath).listFiles()
def versionvalue = { value ->
    def (a,b,c,d) = value.tokenize('.')
    return (a.toInteger()*1000+b.toInteger()*100+c.toInteger()*10+d.toInteger()).toString()
}

mylist.each {
    if(it.isDirectory()){
        def dname = it.getName()
        if(oem=='carestream' && dname =~ /ICAP_.*/){
        droplist.add(dname)
        }
        if(oem=='dental_mind' && dname =~ /Dentalmind_.*/){
            droplist.add(dname)
        }
        if(oem=='wave_pict' && dname =~ /WavePICT .*/){
            droplist.add(dname)
        }
    }
}

for (i in 0..droplist.size()-1) {
    def (name, version) = droplist[i].split(' ')
    droplist[i] = versionvalue(version) + '#' + droplist[i]
}

droplist.sort()

for (i in 0..droplist.size()-1) {
    def (value, it) = droplist[i].split(' ')
    droplist[i] = it
}

return droplist.reverse()