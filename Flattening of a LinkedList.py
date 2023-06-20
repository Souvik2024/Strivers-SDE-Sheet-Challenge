class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
def flatten(root):
    if not root or root.next==None:
        return root
    return merge(root,flatten(root.next))
def merge(a,b):
    res=Node(0)
    temp=res
    while a and b:
        if a.data<b.data:
            temp.bottom=a
            a=a.bottom
        else:
            temp.bottom=b
            b=b.bottom
        temp=temp.bottom
    if a:
        temp.bottom=a
    else:
        temp.bottom=b
    return res.bottom
