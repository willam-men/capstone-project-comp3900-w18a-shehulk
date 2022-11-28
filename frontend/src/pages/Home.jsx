import React from "react";
import { Paper, Typography, Box } from "@mui/material";

import one from "../images/1.jpg";
import two from "../images/2.jpg";
import three from "../images/3.jpg";
import four from "../images/4.jpg";
import five from "../images/5.jpg";
import six from "../images/6.jpg";
import seven from "../images/7.jpg";
import eight from "../images/8.jpg";
import nine from "../images/9.jpg";
import ten from "../images/10.jpg";
import eleven from "../images/11.jpg";
import twelve from "../images/12.jpg";
import thirteen from "../images/13.jpg";
import fourteen from "../images/14.jpg";
import fifteen from "../images/15.jpg";
import sixteen from "../images/recipe.jpg";
import remy from "../images/r.jpg";

export default function Home() {
  const rowone = [one, two, three, four, five, six, seven, eight];
  const rowtwo = [
    nine,
    ten,
    eleven,
    twelve,
    thirteen,
    fourteen,
    fifteen,
    sixteen,
  ];
  const quotes = [
    "If you are what you eat, then I only want to eat the good stuff.",
    "Ratatouille doesn’t sound delicious. It sounds like rat and patootie. Rat-patootie.",
    "What's my problem? First of all, I'm a rat. Which means life is hard. And second, I have a highly developed sense of taste and smell.",
  ];
  const authors = ["- Remy", "- Linguini", "- Remy"];

  const [currQuote, setCurrQuote] = React.useState(quotes[0]);
  const [currAuthor, setCurrAuthor] = React.useState(authors[0]);
  const [count, setCount] = React.useState(0);
  const [topPos, setTopPos] = React.useState(370);
  const [leftPos, setLeftPos] = React.useState("50%");
  const [hoverRemy, setHoverRemy] = React.useState(false);
  const [score, setScore] = React.useState(0);

  React.useEffect(() => {
    const interval = setTimeout(() => {
      const index = parseInt(count) + 1;
      setCurrQuote(quotes[index % 3]);
      setCurrAuthor(authors[index % 3]);
      setCount(index);
    }, 3000);

    return () => clearInterval(interval);
  }, [count]);

  const moveRemy = () => {
    setTopPos(Math.floor(Math.random() * 1000));
    setLeftPos(Math.floor(Math.random() * 1000));
    setScore(parseInt(score) + 1);
  };

  const paperStyle = {
    padding: "100px",
    width: "70vw",
    margin: "50px auto",
    alignItems: "center",
    textAlign: "center",
  };
  const flexStyle = {
    display: "flex",
    flexWrap: "wrap",
    justifyContent: "space-between",
  };
  const middleStyle = {};
  const picStyle = {
    width: "16vw",
    height: "200px",
    objectFit: "cover",
    margin: "10px",
  };
  const titleStyle = { marginTop: "50px" };
  const textStyle = { marginTop: "50px", fontStyle: "italic" };
  const secondTextStyle = {
    marginBottom: "50px",
    fontStyle: "italic",
    marginTop: "10px",
  };
  const instructionStyle = {
    marginTop: "20px",
    marginBottom: "50px",
    fontSize: "14px",
  };

  const easterEggStyle = {
    width: "5px",
    height: "5px",
    transition: "transform 0.15s ease-in-out",
    position: "absolute",
    top: topPos,
    left: leftPos,
  };
  const easterEggHoverStyle = {
    transform: "scale3d(1.05, 1.05, 1)",
    transition: "transform 0.15s ease-in-out",
    position: "absolute",
    top: topPos,
    left: leftPos,
  };

  return (
    <>
      <Paper style={paperStyle}>
        <Typography variant="h4" style={titleStyle}>
          Welcome to Ratatouille!
        </Typography>
        <Typography style={instructionStyle}>
          Hover over Remy and click him to increase your score!
        </Typography>
        <Box style={middleStyle}>
          <Box style={flexStyle}>
            {rowone.map((pic, index) => (
              <Box>
                <img style={picStyle} src={pic} alt="ratatoulle screenshot" />
              </Box>
            ))}
          </Box>
          <Typography style={textStyle}>{currQuote}</Typography>
          <Typography style={secondTextStyle}>{currAuthor}</Typography>
          <Box style={flexStyle}>
            {rowtwo.map((pic, index) => (
              <Box>
                <img style={picStyle} src={pic} alt="ratatoulle screenshot" />
              </Box>
            ))}
          </Box>
          <Typography style={titleStyle}>Current Score: {score}</Typography>
        </Box>
        <img
          src={remy}
          alt="remy easter egg"
          style={hoverRemy ? easterEggHoverStyle : easterEggStyle}
          onMouseEnter={() => setHoverRemy(true)}
          onMouseLeave={() => setHoverRemy(false)}
          onClick={moveRemy}
        />
      </Paper>
    </>
  );
}
