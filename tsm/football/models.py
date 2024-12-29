from django.db import models

class League(models.Model):
    TIER_CHOICES = [
        ("KPL", "Kenyan Premier League"),
        ("NSL", "National Super League")
    ]
    
    tier = models.CharField(max_length=50, choices=TIER_CHOICES)

    def __str__(self):
        return self.tier
    
    
class Team(models.Model):
    name = models.CharField(max_length=200)
    coach = models.CharField(max_length=200)
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='teams')
    #Logo

    # League table data
    matches_played = models.PositiveIntegerField(default=0)
    wins = models.PositiveIntegerField(default=0)
    draws = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    goals_scored = models.PositiveIntegerField(default=0)
    goals_conceded = models.PositiveIntegerField(default=0)
    goal_difference = models.IntegerField(default=0)
    points = models.PositiveIntegerField(default=0)

    def calculate_stats(self):
        """
        calculate all team stats dynamically
        """
        # initialize stats
        points = 0
        wins = 0
        draws = 0
        losses = 0
        goals_scored = 0
        goals_conceded = 0
        matches_played = 0

        matches = Match.objects.filter(models.Q(home_team=self) | models.Q(away_team=self))

        for match in matches:
            matches_played += 1
            if match.home_team == self:
                # Home match stats
                goals_scored += match.home_score
                goals_conceded += match.away_score
                if match.home_score > match.away_score:
                    wins += 1
                    points += 3
                elif match.home_score == match.away_score:
                    draws += 1
                    points += 1
                else:
                    losses += 1
            elif match.away_team == self:
                # Away match stats
                goals_scored += match.away_score
                goals_conceded += match.home_score
                if match.away_score > match.home_score:
                    wins += 1
                    points += 3
                elif match.away_score == match.home_score:
                    draws += 1
                    points += 1
                else:
                    losses += 1

        # update stats
        self.points = points
        self.wins = wins
        self.draws = draws
        self.losses = losses
        self.goals_scored = goals_scored
        self.goals_conceded = goals_conceded
        self.goal_difference = goals_scored - goals_conceded
        self.matches_played = matches_played
    
    def save(self, *args, **kwargs):
        # Recalculate stats before saving
        self.calculate_stats()
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
    
    
class Player(models.Model):
    name = models.CharField(max_length=200)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    position = models.CharField(
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
            ('Postponed', 'Postponed'),
            ],
        default='Scheduled'
    )

    def __str__(self):
        return f"{self.home_team.name} vs {self.away_team.name}"

    def save(self, *args, **kwargs):
        # save the match first
        super().save(*args, **kwargs)

        # Recalculate stats for both teams
        self.home_team.save()
        self.away_team.save()

    