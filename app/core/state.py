class MatchState:
    def __init__(self):
        self.score = 0
        self.wickets = 0
        self.over = 0.0

        self.striker = None
        self.non_striker = None
        self.bowler = None

        self.history = []  # all events
        self.last_ball = None

    def update(self, event: dict):
        runs = event.get("runs", 0)
        wicket = event.get("wicket", False)

        self.score += runs
        if wicket:
            self.wickets += 1

        self.striker = event.get("batsman", self.striker)
        self.bowler = event.get("bowler", self.bowler)

        self.last_ball = event
        self.history.append(event)

        self._update_over(event)

    def _update_over(self, event):
        # simple version (improve later)
        balls = len(self.history)
        self.over = round(balls / 6, 1)

    def snapshot(self):
        return {
            "score": self.score,
            "wickets": self.wickets,
            "over": self.over,
            "striker": self.striker,
            "bowler": self.bowler
        }