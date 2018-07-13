#coding=utf-8
from presentation_layer import page
class NearByPage(page.Page):
    '''聚优惠页面'''

    def __init__(self,d):
        page.Page.__init__(self,d)
        pass

    def img_game(self):
        return self.d(resourceId="PlaneWars")