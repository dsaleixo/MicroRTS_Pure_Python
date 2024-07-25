from __future__ import annotations

import xml.etree.ElementTree as ET

from Game.UnitType import UnitType


'''
 * The physical game state (the actual 'map') of a microRTS game
 *
 * @author santi
 */
'''

from Game.Player import Player
from Game.Unit import Unit
from Game.UnitTypeTable import UnitTypeTable
import numpy as np

class PhysicalGameState :
    
    #Indicates a free tile
    TERRAIN_NONE =0;

    #Indicates a blocked tile
    TERRAIN_WALL=1;
    @staticmethod
    def getTERRAIN_WALL():
        return PhysicalGameState.TERRAIN_WALL

    def __init__(self,width:int=8,height:int=8,terrain =None):
        self._width :int  = width
        self._height : int  = height
        #self._terrain = np.zeros((self._pgs.getWidth(), self._pgs.getHeight()), dtype=np.int8)
        self._terrain  = terrain
        self._players : list[Player] = []
        self._units :dict[int,Unit]= {}
   

    def clone(self):
        Unit.next_ID = 1224
        w = self._width
        h = self._height
        terrain = np.zeros((w, h), dtype=np.int8)
        for t in range(w*h):
            terrain[int(t/w)][int(t%w)]= self._terrain[int(t/w)][int(t%w)]
        
        pgs = PhysicalGameState(w,h,terrain)  
        for p in self._players:
            pgs._players.append(Player(p.getID(), p.getResources()))
        for u2 in self._units.values():
            u = u2.clone()
            pgs.addUnit(u)
        return pgs
            
        
       
        
    
    #Constructs the game state map from a XML
    @staticmethod
    def load( fileName:str, utt:UnitTypeTable)->PhysicalGameState:
        tree = ET.parse(fileName)
        root = tree.getroot()
        return PhysicalGameState.fromXML(root,utt)
       
    def createUnit(self,   a_player :int , a_type: UnitType ,  a_x: int ,  a_y:int ,  a_resources : int):
        
        return Unit(None,a_player,a_type,a_x,a_y,a_resources)
        
    
    def getWidth(self) -> int:
        return self._width       

    def getHeight(self)->int:
        return self._height        

  
    #Sets a new width. This do not change the terrain array, remember to
    #change that when you change the map width or height
    def  setWidth(self, w:int)->None:
        self._width =w    

    #Sets a new height. This do not change the terrain array, remember to
    #change that when you change the map width or height
    def setHeight(self, h:int)->None:
        self._height =h    

    #Returns what is on a given position of the terrain
    def getTerrain(self, x:int,  y:int)->int:
        return self._terrain[x][y]   


    # Puts an entity in a given position of the terrain
    #def setTerrain(self, x:int,  y:int,  v:int)->None:

    #Sets the whole terrain
    def setTerrain(self, t : list[int])->None:
        self._terrain = t    

    
    #Adds a player
    def addPlayer(self, p:Player)->None:
        self._players.append(p)    

        
    #Adds a new {@link Unit} to the map if its position is free
    def addUnit(self, newUnit :Unit)->None:
        self._units[newUnit.getID()]=  newUnit

    #Removes a unit from the map
    def removeUnit(self,u:Unit)->None:
        self._units.pop(u.getID())    
    

    #Returns the list of units in the map
    def getUnits(self) ->dict[int,Unit]: #->map[Unit]
        return self._units    

    #Returns a list of players
    def getPlayers(self)->list[Player]:
        return self._players         

    #Returns a player given its ID
    def getPlayer(self, pID:int)->Player:
        return self._players[pID]    

    #Returns a {@link Unit} given its ID or null if not found
    def getUnit(self, ID:int)->Unit:
        return self._units[ID] if ID in self._units else None

    #Returns the {@link Unit} at a given coordinate or null if no unit is
    #present
    def getUnitAt(self, x:int,  y:int)->Unit:
        for u  in self._units.values():
            if u.getX() == x and u.getY() == y:
                return u
        return None;    

        '''
         * Returns the units within a squared area centered in the given coordinates
         *
         * @param x center coordinate of the square
         * @param y center coordinate of the square
         * @param squareRange square size
         * @return
         */
         //Collection<Unit> getUnitsAround(int x, int y, int squareRange);
         '''
         

    '''
        * Returns units within a rectangular area centered in the given coordinates
        * @param x center coordinate of the rectangle
        * @param y center coordinate of the square
        * @param width rectangle width
        * @param height rectangle height
        * @return
        */
        //Collection<Unit> getUnitsAround(int x, int y, int width, int height);
        '''
       
    '''
        * Returns units within a rectangle with the given top-left vertex and dimensions
        * Tests for x <= unitX < x+width && y <= unitY < y+height
        * Notice that the test is inclusive in top and left but exclusive on bottom and right
        * @param x top left coordinate of the rectangle
        * @param y top left coordinate of the rectangle
        * @param width rectangle width
        * @param height rectangle height
        * @return
        */
        //public Collection<Unit> getUnitsInRectangle(int x, int y, int width, int height);
    '''


    #Returns the winner of the game, given the unit counts or -1 if the game
    def  winner(self)->int:
        unitcounts = [0,0] 
        totalunits = 0;
        for  u in self._units.values():
            
            if u.getPlayer() >= 0: 
                unitcounts[u.getPlayer()]+=1
            
        winner = -1;
        for i in range(2):
            if unitcounts[i] > 0:
                if winner == -1:
                    winner = i;
                else :
                    return -1
        return winner   


    #Returns whether the game is over. The game is over when a player has zero
    # units
    def gameover(self)->bool:
        unitcounts = [0,0] 
        totalunits = 0;
        for  u in self._units.values():
            if u.getPlayer() >= 0: 
                unitcounts[u.getPlayer()]+=1
                totalunits+=1
        

        if totalunits == 0:
            return True
        

        winner = -1;
        for i in range(2):
            if unitcounts[i] > 0:
                if winner == -1:
                    winner = i;
                else :
                    return False;

        return winner != -1;    


    
    #PhysicalGameState clone();

    '''
    * Clone the physical game state, but does not clone the units The terrain
    * is shared amongst all instances, since it never changes
    *
    * @return
    */
    PhysicalGameState cloneKeepingUnits();
    '''
    
    '''
    * Clones the physical game state, including its terrain
    *
    * @return
    */
    PhysicalGameState cloneIncludingTerrain();
    '''
    
    #def toString(self)->str:

    '''    
    * This function tests if two PhysicalGameStates are identical (I didn't
    * name this method "equals" since I don't want Java to use it
    bool equivalents(PhysicalGameState &pgs);
    '''
    
    '''      
    * This function tests if two PhysicalGameStates are identical, including their terrain
    bool equivalentsIncludingTerrain(PhysicalGameState &pgs);
    '''
    
    '''
    * Returns an array with true if the given position has
    * {@link PhysicalGameState.TERRAIN_NONE}
    bool** getAllFree()
    '''
    

    '''
    * Create a compressed String representation of the terrain vector.
    * <p>
    *     The terrain vector is an array of Integers, whose elements only assume 0 and 1 as
    *     possible values. This method compresses the terrain vector by counting the number of
    *     consecutive occurrences of a value and appending this to a String.
    *     Since 0 and 1 may appear in the counter, 0 is replaced by A and 1 is replaced by B.
    * </p>
    * <p>
    *     For example, the String <code>00000011110000000000</code> is transformed into
    *     <code>A6B4A10</code>.
    * </p>
    * <p>
    *     This method is useful when the terrain composes part of a message, to be shared between
    *     client and server.
    * </p>
    *
    * @return compressed String representation of the terrain vector
    */
    string compressTerrain();
    '''
                

    '''
    * Create an uncompressed int array from a compressed String representation of
    * the terrain.
    * @param t a compressed String representation of the terrain
    * @return int array representation of the terrain
    */
    static int* uncompressTerrain(string t);
    '''
    

    '''
        * Writes a XML representation of the map
    //void toxml(XMLWriter w);
    '''

    #void toxml(XMLWriter w, bool includeConstants, bool compressTerrain);
       
   
    #Constructs a map from XML
    @staticmethod
    def fromXML(root, utt)->PhysicalGameState:
        w = int(root.attrib["width"])
        h  = int(root.attrib["height"])
        print(w,h)
        terrain_s = root[0].text
        terrain = np.zeros((w, h), dtype=np.int8)
        for t in range(len(terrain_s)):
            terrain[int(t/w)][int(t%w)]= np.int8(int(terrain_s[t]))
        
        pgs = PhysicalGameState(w,h,terrain)  
        for p in root[1]:
            player = Player.fromXML(p) 
            print(player.toString())
            pgs.addPlayer(player)  
        for u in root[2]:
            unit = Unit.fromXML(u,utt)    
            pgs.addUnit(unit)
            
        return pgs   

   
    '''
         * Transforms a compressed or uncompressed String representation of the terrain into an integer
         * array
         * @param terrainString the compressed or uncompressed String representation of the terrain
         * @param size size of the resulting integer array
         * @return the terrain, in its integer representation
         */
         static vector<int> getTerrainFromUnknownString(string terrainString, int size);

        /**
         * Reset all units HP to their base value
         */
         void resetAllUnitsHP();
    '''