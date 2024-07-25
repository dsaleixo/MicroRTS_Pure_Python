from __future__  import annotations
import numpy as np

from synthesis.extent1DSL.TwoLevelSearch.EvaluateGameState.behavioralFeature import BehavioralFeature

class Feature1:
	def __init__(self, cd : BehavioralFeature = None) :
		self.v = np.zeros(7)
		if cd !=None:
			self.v[0]=cd.getWorker()
			self.v[1]=cd.getLight()
			self.v[2]=cd.getRanged()
			self.v[3]=cd.getHeavy()
			self.v[4]=cd.getBase()
			self.v[5]=cd.getBarrack()
			self.v[6]=cd.getSaved_resource()
	def  toString(self) ->str:
		return str(self.v[0])+"W "+str(self.v[1])+"L "+str(self.v[2])+"R "+str(self.v[3])+"H "+str(self.v[4])+"Ba "+str(self.v[5])+"Br "+str(self.v[6])+"Re"
	
     
	'''
	 @Override
	    public int hashCode() {
	        int code =0;
	        code+= this.v[0];
	        code+= 20*this.v[1];
	        code+= 400*this.v[2];
	        code+= 8000*this.v[3];
	        code+= 160000*this.v[4];
	        code+= 3200000*this.v[5];
	        code+= 64000000*this.v[6];
	       return code;
	    }

	 @Override
	    public boolean equals(Object obj) {
		 Feature1 aux =  (Feature1)obj;
		 
		 if(this.v[0]!=aux.v[0] )return false;
		 if(this.v[1]!=aux.v[1] )return false;
		if(this.v[2]!=aux.v[2] )return false;
		if(this.v[3]!=aux.v[3] )return false;
		if(this.v[4]!=aux.v[4] )return false;
		if(this.v[5]!=aux.v[5]) return false;
		if(this.v[6]!=aux.v[6]) return false;
	
		return true;
	    }
	'''
	def  Clone(self) ->Feature1 :
		nov1 : Feature1=  Feature1()
		for i in range(7):
			nov1.v[i]=self.v[i]
		return nov1



	def semelhaca(self, n :Feature1)->float :
		cont=0
		for i in range(7):
			cont+=1-((1.0*abs( self.v[i]-n.v[i])) /max(max(self.v[i],n.v[i]),1))	
		return cont/7

	def __eq__(self, another):
		if not isinstance(another,Feature1): return False
		if(self.v[0]!=another.v[0] ): return False
		if(self.v[1]!=another.v[1] ): return False
		if(self.v[2]!=another.v[2] ): return False
		if(self.v[3]!=another.v[3] ): return False
		if(self.v[4]!=another.v[4] ): return False
		if(self.v[5]!=another.v[5]) : return False
		if(self.v[6]!=another.v[6]) : return False
	
		return True;
	def __hash__(self):
		code =0;
		code+= self.v[0]
		code+= 20*self.v[1]
		code+= 400*self.v[2]
		code+= 8000*self.v[3]
		code+= 160000*self.v[4]
		code+= 3200000*self.v[5]
		code+= 64000000*self.v[6]
		return hash(code)
	'''
	public int compareTo(Feature n) {
		// TODO Auto-generated method stub
		Feature1 aux = (Feature1) n;
		if(this.v[0]<aux.v[0])return -1;
		if(this.v[0]>aux.v[0])return 1;
		
		if(this.v[1]<aux.v[1])return -1;
		if(this.v[1]>aux.v[1])return 1;
		
		if(this.v[2]<aux.v[2])return -1;
		if(this.v[2]>aux.v[2])return 1;
		
		if(this.v[3]<aux.v[3])return -1;
		if(this.v[3]>aux.v[3])return 1;
		
		if(this.v[4]<aux.v[4])return -1;
		if(this.v[4]>aux.v[4])return 1;
		
		if(this.v[5]<aux.v[5])return 1;
		if(this.v[5]>aux.v[5])return 1;
		
		if(this.v[6]<aux.v[6])return -1;
		if(this.v[6]>aux.v[6])return 1;
		
		return 0;
	}



	@Override
	public int compareTo(Feature1 arg0) {
		// TODO Auto-generated method stub
		return this.compareTo((Feature)arg0) ;
	}
    '''
	
