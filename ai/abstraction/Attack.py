from .AbstractAction import AbstractAction
from Game.Unit import Unit
from Game.UnitAction import UnitAction
from Game.ResourceUsage import ResourceUsage
from Game.GameState import GameState
from Game.AStarPathFinding import AStarPathFinding

class Attack(AbstractAction):

    
    def __init__(self,  u : Unit,  a_target : Unit,  a_pf : AStarPathFinding) :
        super().__init__(u)
        
        self._target = a_target
        self._pf = a_pf
    
    
    
    def completed(self,  gs : GameState) :
       pgs = gs.getPhysicalGameState();
       return pgs.getUnit(self._target.getID())==None;
    
    
    '''
    public boolean equals(Object o)
    {
        if (!(o instanceof Attack)) return false;
        Attack a = (Attack)o;
        return target.getID() == a.target.getID() && pf.getClass() == a.pf.getClass();
    }
   
    
    public void toxml(XMLWriter w)
    {
        w.tagWithAttributes("Attack","unitID=\""+unit.getID()+"\" target=\""+target.getID()+"\" pathfinding=\""+pf.getClass().getSimpleName()+"\"");
        w.tag("/Attack");
    }
     '''

    def toString(self):
        return self._unit.toSting() + " attack " + self._target.toString()


    def execute(self, gs : GameState,  ru: ResourceUsage)->UnitAction :
        
        dx = self._target.getX()-self._unit.getX();
        dy = self._target.getY()-self._unit.getY();
        d = (dx*dx+dy*dy)**0.5;
        if d<=self._unit.getAttackRange():
            return  UnitAction.build_Attack( self._target.getX(),self._target.getY())
        else :
            move = self._pf.findPathToPositionInRange(self._unit, self._target.getX()+self._target.getY()*gs.getPhysicalGameState().getWidth(), self._unit.getAttackRange(), gs);
            if move.getType()!=UnitAction.getTYPE_NONE()   and gs.isUnitActionAllowed(self._unit, move): return move
            return None;
       