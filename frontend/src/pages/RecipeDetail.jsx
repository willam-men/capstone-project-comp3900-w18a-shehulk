import {
  Typography,
  Paper,
  CircularProgress,
  Box,
  Button,
  Breadcrumbs,
  Link,
  Avatar,
  Tooltip,
  IconButton,
  Grid,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  TextField,
  Rating,
} from "@mui/material";
import FavoriteIcon from "@mui/icons-material/Favorite";
import { useParams, useNavigate } from "react-router-dom";
import React from "react";
import fetchData from "../helper.js";

import RecipeCard from "../components/RecipeCard.jsx";
import defaultRecipePic from "../images/recipe.jpg";
import CommentsList from "../components/CommentList.jsx";
import defaultPic from "../images/remy.jpg";

import SoupKitchenIcon from "@mui/icons-material/SoupKitchen";
import CoffeeIcon from "@mui/icons-material/Coffee";
import CakeIcon from "@mui/icons-material/Cake";
import CookieIcon from "@mui/icons-material/Cookie";
import BreakfastDiningIcon from "@mui/icons-material/BreakfastDining";
import DinnerDiningIcon from "@mui/icons-material/DinnerDining";
import RiceBowlIcon from "@mui/icons-material/RiceBowl";

export default function RecipeDetail() {
  const params = useParams();
  const navigate = useNavigate();
  const token = localStorage.getItem("token");
  const recipeId = params.recipeid;

  const [recipeDetail, setRecipeDetail] = React.useState(null);
  const [loading, setLoading] = React.useState(true);
  const [servings, setServings] = React.useState(null);
  const [ingredients, setIngredients] = React.useState(null);
  const [recipePic, setRecipePic] = React.useState(null);
  const [isLiked, setIsLiked] = React.useState(false);
  const [numLikes, setNumLikes] = React.useState(0);
  const [comments, setComments] = React.useState([]);
  const [reccomendations, setReccomendations] = React.useState([]);
  const [openAddComment, setOpenAddComment] = React.useState(false);
  const [userRating, setUserRating] = React.useState(0);
  const [userComment, setUserComment] = React.useState(null);
  const [updateComments, setUpdateComments] = React.useState(false);
  const [finishedLoading, setFinishedLoading] = React.useState(false);

  const [authorIsHover, setAuthorIsHover] = React.useState(false);

  async function loadRecipe() {
    const data = await fetchData(
      "GET",
      `api/recipe?recipeId=${recipeId}`,
      {},
      token
    );
    return data;
  }

  async function loadReccommendations() {
    const data = await fetchData(
      "GET",
      `api/recommended_recipes?recipeId=${recipeId}`,
      {},
      token
    );
    return data;
  }

  async function getComments() {
    const data = await fetchData("GET", `api/${recipeId}/comments`);
    return data;
  }

  React.useEffect(() => {
    async function loadreceipts() {
      window.scrollTo(0, 0);
      const recipeOutput = await loadRecipe();
      setFinishedLoading(true);
      if ("code" in recipeOutput) {
        navigate("/notfound");
      } else {
        const recs = await loadReccommendations();
        setReccomendations(recs);
        const commentOutput = await getComments();
        setComments(commentOutput);
        setRecipeDetail(recipeOutput);
        setServings(recipeOutput.servings);
        setIngredients(recipeOutput.ingredients);
        setIsLiked(recipeOutput.isLiked);
        setNumLikes(recipeOutput.likes);
        setRecipePic(recipeOutput.photo);
        setLoading(false);
      }
    }
    loadreceipts();
  }, [params]);

  React.useEffect(() => {
    async function updateComs() {
      if (finishedLoading) {
        const commentOutput = await getComments();
        setComments(commentOutput);
      }
    }
    updateComs();
  }, [updateComments]);

  const addServe = () => {
    const serves = parseInt(servings) + 1;
    editServes(serves);
  };

  const subtractServe = () => {
    const serves = parseInt(servings) - 1;
    if (serves > 0) {
      editServes(serves);
    } else {
      alert("serving size must be bigger than 0");
    }
  };

  const editServes = (serves) => {
    const ogServes = parseInt(recipeDetail.servings);
    setServings(serves);
    setIngredients([]);
    for (let i = 0; i < recipeDetail.ingredients.length; i++) {
      const newQuantity = (
        (parseFloat(recipeDetail.ingredients[i].quantity) / ogServes) *
        serves
      ).toFixed(2);
      if (!isNaN(newQuantity)) {
        setIngredients((ingredients) => [
          ...ingredients,
          {
            quantity: newQuantity,
            units: recipeDetail.ingredients[i].units,
            ingredient: recipeDetail.ingredients[i].ingredient,
          },
        ]);
      } else {
        setIngredients((ingredients) => [
          ...ingredients,
          {
            quantity: null,
            units: null,
            ingredient: recipeDetail.ingredients[i].ingredient,
          },
        ]);
      }
    }
  };

  const handleLike = () => {
    if (isLiked) {
      // unlike
      fetchData("POST", "api/unlike", { recipeId: recipeId }, token);
      setNumLikes(parseInt(numLikes) - 1);
      setIsLiked(false);
    } else {
      // like
      fetchData("POST", "api/like", { recipeId: recipeId }, token);
      setNumLikes(parseInt(numLikes) + 1);
      setIsLiked(true);
    }
  };

  const navigateToMealSearch = () => {
    navigate(`/search/mealtypes=${recipeDetail.mealType}`);
  };

  const postCommentRating = () => {
    setOpenAddComment(false);

    // post the comment
    fetchData(
      "POST",
      `api/${recipeId}/comment`,
      { token: token, comment: userComment, rating: userRating },
      token
    );
    setUpdateComments(!updateComments);
    setUserRating(0);
  };

  const computeIcon = (mealType) => {
    switch (mealType) {
      case "Starter":
        return <SoupKitchenIcon />;
      case "Beverage":
        return <CoffeeIcon />;
      case "Breakfast":
        return <BreakfastDiningIcon />;
      case "Dessert":
        return <CakeIcon />;
      case "Main":
        return <DinnerDiningIcon />;
      case "Snack":
        return <CookieIcon />;
      case "Side":
        return <RiceBowlIcon />;
      default:
        return;
    }
  };

  const breadcrumbsMargin = { marginBottom: "70px" };
  const pageStyle = { padding: "100px", textAlign: "left" };
  const flexBoxStyle = { display: "flex", justifyContent: "flex-end" };
  const methodStyle = { display: "flex", margin: "10px" };
  const methodNumStyle = { marginRight: "20px" };
  const horiListSpacing = { marginLeft: "5px" };
  const servingStyle = {
    display: "flex",
    margin: "20px",
    gap: "20px",
    textAlign: "center",
    justifyContent: "center",
  };
  const servingText = { margin: "20px" };
  const ingredStyle = {
    display: "flex",
    margin: "5px",
    textAlign: "center",
    justifyContent: "center",
  };
  const unitStyle = { marginRight: "5px" };
  const ingred = { marginRight: "10px" };

  const likedStyle = { padding: "20px", color: "red" };
  const unlikedStyle = { padding: "20px", color: "black" };
  const imageStyle = {
    width: "100%",
    height: "400px",
    objectFit: "cover",
    marginBottom: "50px",
  };
  const titleDescBoxStyle = {
    textAlign: "left",
    marginTop: "50px",
    marginBottom: "50px",
  };
  const avatarStyle = { width: "80px", height: "80px", marginTop: "20px" };
  const authorBoxStyle = {
    display: "flex",
    transition: "transform 0.15s ease-in-out",
  };
  const authorBoxHoverStyle = {
    display: "flex",
    cursor: "pointer",
    transform: "scale3d(1.05, 1.05, 1)",
    transition: "transform 0.15s ease-in-out",
  };
  const authorCredStyle = {
    textAlign: "left",
    marginTop: "40px",
    marginLeft: "20px",
  };
  const mealTypeButtonStyle = { padding: "0px 40px" };
  const flexStyle = {
    display: "flex",
    justifyContent: "space-between",
    textAlign: "right",
  };
  const infoBoxStyle = {
    padding: "20px",
    border: "3px solid white",
    borderRadius: "25px",
    width: "60%",
    marginBottom: "50px",
    verticalAlign: "middle",
  };
  const infoBoxSmallStyle = {
    padding: "20px",
    border: "3px solid white",
    borderRadius: "25px",
    width: "30%",
    marginBottom: "50px",
    textAlign: "center",
  };
  const infoBoxFillStyle = {
    padding: "20px",
    border: "3px solid white",
    borderRadius: "25px",
    width: "96%",
    marginBottom: "50px",
  };
  const infoDetailsStyle = { padding: "50px" };
  const textAlignLeft = { textAlign: "left" };
  const textAlignCenter = { textAlign: "center" };
  const boxStyle = {
    margin: "10px",
    display: "flex",
    justfyContent: "center",
    alignItems: "center",
    width: "100%",
  };
  const subtitleStyle = { padding: "30px", textAlign: "center" };
  const commentButtonStyle = {
    paddingBottom: "30px",
    alignItems: "center",
    textAlign: "center",
  };
  const commentInputStyle = { marginTop: "10px" };

  return (
    <>
      {loading ? (
        <Box sx={{ display: "flex" }}>
          <CircularProgress />
        </Box>
      ) : (
        <Paper style={pageStyle}>
          <Breadcrumbs aria-label="breadcrumb" style={breadcrumbsMargin}>
            <Link
              underline="hover"
              color="inherit"
              onClick={() => navigate("/explore")}
            >
              All Recipes
            </Link>
            <Typography color="text.primary">{recipeDetail.title}</Typography>
          </Breadcrumbs>

          {recipePic ? (
            <Box component="img" style={imageStyle} src={recipePic} />
          ) : (
            <Box component="img" style={imageStyle} src={defaultRecipePic} />
          )}

          <Paper style={infoBoxFillStyle}>
            <Box style={titleDescBoxStyle}>
              <Typography variant="h2">{recipeDetail.title}</Typography>
              <Typography variant="h6">{recipeDetail.description}</Typography>
            </Box>
          </Paper>

          <Box style={flexStyle}>
            <Paper style={infoBoxSmallStyle}>
              <Box
                style={authorIsHover ? authorBoxHoverStyle : authorBoxStyle}
                onClick={() => {
                  navigate(`/profile/${recipeDetail.authorId}`);
                }}
                onMouseEnter={() => setAuthorIsHover(true)}
                onMouseLeave={() => setAuthorIsHover(false)}
              >
                {recipeDetail.authorPfp ? (
                  <Avatar
                    style={avatarStyle}
                    alt="user's profile picture"
                    src={recipeDetail.authorPfp}
                  />
                ) : (
                  <Avatar
                    style={avatarStyle}
                    alt="user's profile picture"
                    src={defaultPic}
                  />
                )}
                <Box style={authorCredStyle}>
                  <Typography>{recipeDetail.authorName}</Typography>
                  {recipeDetail.authorTitle ? (
                    <Typography>{recipeDetail.authorTitle}</Typography>
                  ) : (
                    <Typography>Aspiring Masterchef</Typography>
                  )}
                </Box>
              </Box>

              <Tooltip title="Like">
                <IconButton aria-label="add to favorites">
                  <FavoriteIcon
                    style={isLiked ? likedStyle : unlikedStyle}
                    onClick={handleLike}
                  />
                  <Typography>{numLikes} likes</Typography>
                </IconButton>
              </Tooltip>

              <Tooltip title="See All Recipes Of This Meal Type">
                <Button
                  style={mealTypeButtonStyle}
                  onClick={navigateToMealSearch}
                  startIcon={computeIcon(recipeDetail.mealType)}
                >
                  {recipeDetail.mealType}
                </Button>
              </Tooltip>

              {recipeDetail.ratings && (
                <Rating
                  defaultValue={recipeDetail.ratings}
                  precision={0.5}
                  readOnly
                />
              )}
            </Paper>

            <Paper style={infoBoxStyle}>
              <Box style={infoDetailsStyle}>
                <Typography style={flexBoxStyle}>
                  Cuisines:{" "}
                  {recipeDetail.cuisine
                    .filter(
                      (_, index) => index !== recipeDetail.cuisine.length - 1
                    )
                    .map((cuisine) => (
                      <Typography style={horiListSpacing}>
                        {cuisine},{" "}
                      </Typography>
                    ))}
                  {recipeDetail.cuisine
                    .filter(
                      (_, index) => index === recipeDetail.cuisine.length - 1
                    )
                    .map((cuisine) => (
                      <Typography style={horiListSpacing}>
                        {cuisine}{" "}
                      </Typography>
                    ))}
                </Typography>
                {recipeDetail.dietaries.length === 0 ? (
                  <Typography></Typography>
                ) : (
                  <Typography style={flexBoxStyle}>
                    Dietaries:{" "}
                    {recipeDetail.dietaries
                      .filter(
                        (_, index) =>
                          index !== recipeDetail.dietaries.length - 1
                      )
                      .map((dietary, i) => (
                        <Typography style={horiListSpacing}>
                          {dietary},
                        </Typography>
                      ))}
                    {recipeDetail.dietaries
                      .filter(
                        (_, index) =>
                          index === recipeDetail.dietaries.length - 1
                      )
                      .map((dietary, i) => (
                        <Typography style={horiListSpacing}>
                          {dietary}
                        </Typography>
                      ))}
                  </Typography>
                )}
                <Typography>Prep Time: {recipeDetail.prepTime}</Typography>
                <Typography>Cooking Time: {recipeDetail.cookTime}</Typography>
                <Typography>Difficulty: {recipeDetail.difficulty}</Typography>
              </Box>
            </Paper>
          </Box>

          <Box style={flexStyle}>
            <Paper style={infoBoxStyle}>
              <Typography variant="h5" style={textAlignCenter}>
                Ingredients:{" "}
              </Typography>
              <div style={servingStyle}>
                <Tooltip title="Subtract A Serving">
                  <Button
                    variant="outlined"
                    onClick={() => {
                      subtractServe();
                    }}
                  >
                    -
                  </Button>
                </Tooltip>

                <Typography style={servingText}>
                  Servings: {servings}
                </Typography>
                <Tooltip title="Add Another Serving">
                  <Button
                    variant="outlined"
                    onClick={() => {
                      addServe();
                    }}
                  >
                    +
                  </Button>
                </Tooltip>
              </div>

              {ingredients.map((ingredient, i) => (
                <div style={ingredStyle}>
                  <Typography style={unitStyle}>
                    {ingredient.quantity}
                  </Typography>
                  <Typography style={ingred}>{ingredient.units}</Typography>
                  <Typography>{ingredient.ingredient}</Typography>
                </div>
              ))}
            </Paper>
            <Paper style={infoBoxSmallStyle}>
              <Box>
                <Typography variant="h5">Utensils: </Typography>
                {recipeDetail.utensils.map((utensil, i) => (
                  <Typography>{utensil}</Typography>
                ))}
              </Box>
            </Paper>
          </Box>

          <Paper style={infoBoxFillStyle}>
            <Box style={textAlignLeft}>
              <Typography variant="h5">Method: </Typography>
              {recipeDetail.method.map((method, i) => (
                <div style={methodStyle}>
                  <Typography style={methodNumStyle}>{i + 1}</Typography>
                  <Typography>{method}</Typography>
                </div>
              ))}
            </Box>
          </Paper>

          <Paper style={infoBoxFillStyle}>
            <Box style={textAlignCenter}>
              <Typography variant="h5" style={subtitleStyle}>
                More Delicious Ideas:{" "}
              </Typography>
              {reccomendations.length !== 0 ? (
                <Box style={boxStyle}>
                  <Grid
                    container
                    spacing={{ xs: 2, md: 3 }}
                    columns={{ xs: 4, sm: 8, md: 12 }}
                    direction="row"
                    alignItems="center"
                    justifyContent="center"
                  >
                    {reccomendations.map((recipe, index) => {
                      return (
                        <Grid
                          item
                          xs={2}
                          sm={4}
                          md={4}
                          key={index}
                          display="flex"
                          justifyContent="center"
                          alignItems="center"
                        >
                          <RecipeCard recipe={recipe} />
                        </Grid>
                      );
                    })}
                  </Grid>
                </Box>
              ) : (
                <Typography>
                  No reccomendations since no ingredients match
                </Typography>
              )}
            </Box>
          </Paper>
          <Paper style={infoBoxFillStyle}>
            <Typography style={subtitleStyle} variant="h5">
              Comments and Ratings
            </Typography>
            {token ? (
              <Box style={commentButtonStyle}>
                <Button
                  variant="outlined"
                  onClick={() => setOpenAddComment(true)}
                >
                  Add A Comment Or Rating
                </Button>
              </Box>
            ) : (
              <Box style={commentButtonStyle}>
                <Button onClick={() => navigate("/login")}>
                  Please Login To Add A Comment
                </Button>
              </Box>
            )}

            <CommentsList
              comments={comments}
              setUpdateComments={setUpdateComments}
              updateComments={updateComments}
            />
          </Paper>

          <Dialog
            open={openAddComment}
            onClose={() => setOpenAddComment(false)}
            aria-labelledby="add-comments-dialog"
            aria-describedby="add-comments-dialog"
            fullWidth
            maxWidth="md"
          >
            <DialogTitle>Add a comment for {recipeDetail.title}</DialogTitle>
            <DialogContent>
              <TextField
                fullWidth
                label="Add A Comment"
                style={commentInputStyle}
                onChange={(e) => setUserComment(e.target.value)}
              />
              <Rating
                style={commentInputStyle}
                size="large"
                precision={0.5}
                value={userRating}
                onChange={(e, newValue) => {
                  setUserRating(newValue);
                }}
              />
            </DialogContent>
            <DialogActions>
              <Button variant="contained" onClick={postCommentRating}>
                Post Comment
              </Button>
            </DialogActions>
          </Dialog>
        </Paper>
      )}
    </>
  );
}
