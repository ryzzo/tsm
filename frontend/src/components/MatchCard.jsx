import React from "react";
import { Card, Row, Col } from 'react-bootstrap';

const MatchCard = ({ home_team, home_score, away_team, away_score, time }) => {

    return(
        <Card className="p-3">
            <Card.Body>
            <Row className="align-items-center text-center">  
                </Row>
                <Row className="align-items-center text-center">
                    <Col xs={4} className="text-start">
                        <h5>{home_team}</h5>
                    </Col>
                    <Col xs={4} className="text-center">
                        <h4>{home_score || ''} - {away_score || ''}</h4>
                    </Col>
                    <Col xs={4} className="text-end">
                        <h5>{away_team}</h5>
                    </Col>
                </Row>
                <Row className="align-items-center text-center">
                    <Col>
                        {time}
                    </Col>   
                </Row>
            </Card.Body>
        </Card>
    )
};

export default MatchCard;