import os


def parse_dependencies(metafile):
    dependencies=[]
    for line in file(metafile).readlines():
        split=line.strip().split("=",1)
        if len(split)==2 and split[0]=="PKG_DEPENDS":
            value=split[1].strip('"')
            if value[:12]=="$PKG_DEPENDS":
                value=value[12:]
            if value != "":
                dependencies.extend(value.split())
    return dependencies
    
def get_dependencies(target):
    pkg_dependencies={}
    for root,dirs,files in os.walk(target):
        if "meta" in files:
            dependencies=parse_dependencies(os.path.join(root,"meta"))
            package=os.path.basename(root)
            pkg_dependencies[package]=dependencies
    return pkg_dependencies

if __name__ == "__main__":
    pkg_dependencies=get_dependencies("packages")
    for k in pkg_dependencies.keys():
        print "%s: %s" % (k," ".join(pkg_dependencies[k]))
