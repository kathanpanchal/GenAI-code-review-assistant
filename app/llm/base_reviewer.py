from abc import ABC, abstractmethod


class BaseReviewer(ABC):

    @abstractmethod
    def review_diff(self, diff_text):
        pass