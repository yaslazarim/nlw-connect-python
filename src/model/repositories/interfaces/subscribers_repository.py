from abc import ABC, abstractmethod
from src.model.entities.inscritos import Inscritos

class SubscribersRepositoryInterface(ABC):
    
    @abstractmethod
    def insert(self, subscriber_info: dict) -> None: pass
    
    @abstractmethod
    def select_subscriber(self,  email: str, subscriber_info: int) -> Inscritos: pass
<<<<<<< HEAD
    
    @abstractmethod
    def select_susbscribers_by_link(self, link: str, event_id: str) -> list: pass
    
    @abstractmethod
    def get_ranking(self, event_id: int) -> list: pass

=======
        
>>>>>>> 92e3d972337966e3a0da0e8cbe4e31eeff6f0d57
