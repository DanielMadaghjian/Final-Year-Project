class Sentiment_score:
    def __init__(self, total, positive, negative, strong, weak, active, passive,famine_terms, grain_terms, processed_grains_terms, livestock_terms, potatoes_terms, hay_terms):
        self.total = total
        self.positive = positive
        self.negative = negative
        self.strong = strong
        self.weak = weak
        self.active = active
        self.passive = passive
        self.famine_terms = famine_terms
        self.grains_terms = grain_terms
        self.processed_grains_terms = processed_grains_terms
        self.livestock_terms = livestock_terms
        self.potatoes_terms = potatoes_terms
        self.hay_terms = hay_terms