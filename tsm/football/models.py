from django.db import models

class League(models.Model):
    TIER_CHOICES = (
        ('1', 'Kenyan Premier League')
        ('2', 'Kenyan National Premier League')
    )
    name = models.CharField(max_length=200)
    tier = models.CharField(max_length=50, choices=TIER_CHOICES)

    def __str__(self):
        return self.name
    
class Team(models.Model):
    name = models.CharField(max_length=200)
    League = models.ForeignKey(League, on_delete=models.CASCADE, related_name='teams')

    # League table data
    matches_played = models.PositiveIntegerField(default=0)
    wins = models.PositiveIntegerField(default=0)
    draws = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    goals_scored = models.PositiveIntegerField(default=0)
    goals_conceded = models.PositiveIntegerField(default=0)
    goal_difference = models.IntegerField(default=0)
    points = models.PositiveIntegerField(default=0)

    def update_stats(self, match_result):
        """
        Updates the team stats based on a match result.
        Example match_result = {'goals_for': 2, 'goals_against': 1, 'result': 'win'}
        """
        self.matches_played += 1
        self.goals_scored += match_result['goals_for']
        self.goals_conceded += match_result['goals_against']
        self.goal_difference = self.goals_scored - self.goals_conceded

        if match_result['result'] == 'win':
            self.wins += 1
            self.points += 3
        elif match_result['result'] == 'draw':
            self.draws += 1
            self.points += 1
        elif match_result['result'] == 'loss':
            self.losses += 1

        self.save()

    def __str__(self):
        return self.name
    
class Players(models.Model):
    name = models.CharField(max_length=200)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    choices = models.CharField(
        max_length=50,
        choices=[
            ('Goalkeeper', 'Goalkeeper'), 
            ('Defender', 'Defender'), 
            ('Midfielder', 'Midfielder'), 
            ('Forward', 'Forward')
        ]
    )

    def __str__(self):
        return self.name
    

class Match(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='matches')
    date = models.DateTimeField()
    home_score = models.PositiveIntegerField(blank=True, null=True)
    away_score = models.PositiveIntegerField(blank=True, null=True)
    status = models.CharField(
        max_length=50, 
        choices=[
            ('Scheduled', 'Scheduled'),
            ('Completed', 'Completed'),
            ('Postponed', 'Postponed')
            ],
        default='Scheduled'
    )

    def __str__(self):
        return f"{self.home_team.name} vs {self.away_team.name}"