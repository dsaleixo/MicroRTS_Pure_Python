

from Game.PhysicalGameState import  PhysicalGameState
from Game.GameState import GameState
from Game.Unit import Unit
from Game.UnitAction import  UnitAction
from synthesis.baseDSL.almostTerminal.almostTerminal import AlmostTerminal


from synthesis.baseDSL.util.factory import Factory



class Direction(AlmostTerminal):
    
   
    def __init__(self,direc= None) -> None:
        self._direc = direc
    
    
    def rules(self):#->list[str]:
        return ["Right",
		        "Left",
                "Up",
                "Down",
		        "EnemyDir"]
    
   
    
    def setValue(self, s :str)->None:
        self._direc=s
    
    def getValue(self)->str:
        return self._direc
	
    def translate(self)->str:
        return self._direc
    
    
    
    def converte(self,gs : GameState, player:int, u : Unit) -> int :
        x = u.getX()
        y = u.getY()
        pgs = gs.getPhysicalGameState()
        height = pgs.getHeight() - 1
        width = pgs.getWidth() - 1
        if self._direc == "Right" and (x+1) +(y)*width< height*width and (x+1) +(y)*width>= 0:
            if gs.free(x+1,y):return UnitAction.getDIRECTION_RIGHT()
        if self._direc == "Left" and  (x-1) +(y)*width< height*width and (x-1) +(y)*width>= 0:
            if gs.free(x-1,y):return UnitAction.getDIRECTION_LEFT()
        if self._direc == "Up" and (x) +(y-1)*width< height*width and (x) +(y-1)*width>= 0:
            if gs.free(x,y-1):return UnitAction.getDIRECTION_UP()
        if self._direc == "Down" and  (x) +(y+1)*width< height*width and (x) +(y+1)*width>= 0:
            if gs.free(x,y+1):return UnitAction.getDIRECTION_DOWN()
        
        if self._direc == "EnemyDir" :
            pgs = gs.getPhysicalGameState()
            best_direction = -1
            best_score = -1
	        
            if y>0 and gs.free(x,y-1): 
                score = self.score(x,y-1, player, pgs)
                if score<best_score or best_direction==-1 :
                    best_score = score
                    best_direction = UnitAction.getDIRECTION_UP()
	            
            if x<pgs.getWidth()-1 and gs.free(x+1,y):
                score = self.score(x+1,y, player, pgs)
                if score<best_score or best_direction==-1 :
                    best_score = score
                    best_direction = UnitAction.getDIRECTION_RIGHT()        
	            
            if y<pgs.getHeight()-1 and gs.free(x,y+1) :
                score = self.score(x,y+1, player, pgs)
                if score<best_score or best_direction==-1 :
                    best_score = score
                    best_direction = UnitAction.getDIRECTION_DOWN()
	    
            if x>0 and gs.free(x-1,y): 
                score = self.score(x-1,y, player, pgs)
                if score<best_score or best_direction==-1:
                    best_score = score
                    best_direction = UnitAction.getDIRECTION_LEFT()
            return best_direction
        return -1
	
 
 
    def score(self, x:int, y: int, player: int, pgs: PhysicalGameState) -> int:
        distance = 0
        first = True
        #score is minus distance to closest resource
        for u in pgs.getUnits(1-player).values():
                dx = abs(u.getX() - x) 
                dy = abs(u.getY() - y)
                d = dx*dx +dy*dy
                if  first or d<distance :
                    distance = d
                    first = False
        return distance
	    
    def clone(self, f: Factory):
        return f.build_Direction(self.getValue())