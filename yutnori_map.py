# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""




class Map():
    """
    gksrmfdl dkscuwla.
    
    map_index
    
    -15 -14 -13 -12 -11 -10
    
    -16 -23         -24 - 9
    
    -17     -22  -25    - 8
    
              -28       
    
    -18     -26  -21    - 7   
         
    -19 -27         -20 - 6
    
    - 0 - 1 - 2 - 3 - 4 - 5
    0 is start point.
    
    """
    
    def __init__(self):
        """
        self.map_list[map_index][0~3]
        - '0'
            True: when the direction will be changed.
            False: Other case.
            
        - '1'
            the direction about route on center.
        
        - '2'
            the piece of owner in each node.
        
        - '3'
            the number of pieces in each node.
            
        """
        self.map_list = [[False, None, -1, 0], [False, None, -1, 0], [False, None, -1, 0], [False, None, -1, 0], [True, None, -1, 0],
                          [False, 'up', -1, 0], [False, None, -1, 0], [False, None, -1, 0], [False, None, -1, 0], [True, None, -1, 0],
                          [False, 'down', -1, 0], [False, None, -1, 0], [False, None, -1, 0], [False, None, -1, 0], [None, None, -1, 0],
                          [False, None, -1, 0], [False, None, -1, 0], [False, None, -1, 0], [False, None, -1, 0], [None, None, -1, 0],
                          [False, 'up', -1, 0], [False, 'up', -1, 0], [False, 'up', -1, 0], [False, 'up', -1, 0],
                          [False, 'down', -1, 0], [False, 'down', -1, 0], [False, 'down', -1, 0], [False, 'down', -1, 0],
                          [True, None, -1, 0]]
        
        self.user_remained = [4, 4, 4, 4]
        self.in_goal = [0, 0, 0, 0]
        self.winner = -1
    def select(self, n_roll, map_index, user_info):
        """
        - 'map_index'
            the node selected by user.
            
        - 'n_roll'
            the result of roll.
            
        - 'user_info'
            index about users.
        """
        self.user_info = user_info
        self.n_roll = n_roll
        
        if map_index == 0 and self.user_remained[user_info] > 0:
            self.map_list[map_index][2] = user_info
            self.map_list[map_index][3] = 1
            self.user_remained[user_info] = self.user_remained[user_info] - 1
            
        if self.map_list[map_index][2] != user_info:
            raise ValueError("YOU SELECTED A WRONG NODE")
        
        if map_index == len(self.map_list) - 1:
            if self.map_list[map_index][1] == 'up':
                if n_roll <= 2:
                    self.change_info(map_index, 21 + n_roll)
                else:
                    self.change_info(map_index, 12 + n_roll)
            
            elif self.map_list[map_index][1] == 'down':
                if n_roll <= 2:
                    self.change_info(map_index, 25 + n_roll)
                else:
                    self.change_info(map_index, (17 + n_roll)%20)
                    
        elif not self.map_list[map_index][0] and self.map_list[map_index][1] == None:
            self.change_info(map_index, (map_index + n_roll)%20)
        
        elif self.map_list[map_index][0] == True:
            if self.map_list[map_index][1] == 'up':
                if n_roll == 3:
                    self.change_info(map_index, len(self.map_list) - 1)
                elif n_roll < 3:
                    self.change_info(map_index, 19 + n_roll)
                else :
                    self.change_info(map_index, 21 + n_roll)
                    
        elif self.map_list[map_index][0] == True:
            if self.map_list[map_index][1] == 'up':
                if n_roll == 3:
                    self.change_info(map_index, len(self.map_list) - 1)
                elif n_roll < 3:
                    self.change_info(map_index, 19 + n_roll)
                else :
                    self.change_info(map_index, 21 + n_roll)
                    
            if self.map_list[map_index][1] == 'down':
                if n_roll == 3:
                    self.change_info(map_index, len(self.map_list) - 1)
                elif n_roll < 3:
                    self.change_info(map_index, 23 + n_roll)
                else :
                    self.change_info(map_index, 25 + n_roll)
        
        elif self.map_list[map_index][1] == 'up':
            if map_index == 20 or map_index ==21:
                if map_index + n_roll == 22:
                    self.change_info(map_index, len(self.map_list) - 1)
                elif map_index + n_roll < 22:
                    self.change_info(map_index, map_index + n_roll)
                elif map_index + n_roll < 25:
                    self.change_info(map_index, map_index + n_roll - 1)
                else:
                    self.change_info(map_index, map_index + n_roll - 10)
                    
            if map_index == 22 or map_index == 23:
                if map_index + n_roll < 24:
                    self.change_info(map_index, map_index + n_roll)
                else:
                    self.change_info(map_index, map_index + n_roll - 9)
                    
        elif self.map_list[map_index][1] == 'up':
            if map_index == 24 or map_index ==25:
                if map_index + n_roll == 26:
                    self.change_info(map_index, len(self.map_list) - 1)
                elif map_index + n_roll < 26:
                    self.change_info(map_index, map_index + n_roll)
                elif map_index + n_roll < 29:
                    self.change_info(map_index, map_index + n_roll - 1)
                else:
                    self.change_info(map_index, map_index + n_roll - 29)
                    
            if map_index == 26 or map_index == 27:
                if map_index + n_roll < 28:
                    self.change_info(map_index, map_index + n_roll)
                else:
                    self.change_info(map_index, map_index + n_roll - 28)
              
        
        return self.map_list, self.winner, self.user_info
        
    def change_info(self, departure, destination):
        
        if destination == 0:
            self.in_goal[self.user_info] = self.in_goal[self.user_info] + self.map_list[departure][3]
            
            
        elif destination == 28:
            self.map_list[destination][1] = self.map_list[departure][1]
            
        if self.map_list[destination][2] == self.map_list[departure][2]:
                self.map_list[destination][3] = self.map_list[destination][3] + self.map_list[departure][3]
                self.map_list[destination][2] = self.map_list[departure][2]
                self.map_list[departure][2] = -1
                self.map_list[departure][3] = 0
                
        else:
                self.map_list[destination][2] == self.map_list[departure][2]
                self.map_list[destination][3] = self.map_list[departure][3]
                self.map_list[destination][2] = self.map_list[departure][2]
                self.map_list[departure][2] = -1
                self.map_list[departure][3] = 0
        
        if self.in_goal[self.user_info] == 4:
                self.winner = self.user_info
    
        if self.n_roll < 4:
            self.user_info = (self.user_info + 1)%4
            



ad = Map()
print(ad.select(5, 0, 0))













