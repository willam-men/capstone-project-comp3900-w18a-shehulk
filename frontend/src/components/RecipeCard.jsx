import React from "react";
import fetchData from "../helper.js";
import { useNavigate } from "react-router-dom";
import {
  Tooltip,
  Typography,
  Dialog,
  Box,
  Button,
  Avatar,
  CircularProgress,
  Card,
  CardContent,
  CardHeader,
  CardMedia,
  CardActions,
  IconButton,
  DialogActions,
  DialogTitle,
  DialogContent,
} from "@mui/material";
import FavoriteIcon from "@mui/icons-material/Favorite";
import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete";
import MenuBookIcon from "@mui/icons-material/MenuBook";
import ArrowForwardIosIcon from "@mui/icons-material/ArrowForwardIos";
import CloseIcon from "@mui/icons-material/Close";
import DoneIcon from "@mui/icons-material/Done";
import AddIcon from "@mui/icons-material/Add";
import RemoveIcon from "@mui/icons-material/Remove";

import SoupKitchenIcon from "@mui/icons-material/SoupKitchen";
import CoffeeIcon from "@mui/icons-material/Coffee";
import CakeIcon from "@mui/icons-material/Cake";
import CookieIcon from "@mui/icons-material/Cookie";
import BreakfastDiningIcon from "@mui/icons-material/BreakfastDining";
import DinnerDiningIcon from "@mui/icons-material/DinnerDining";
import RiceBowlIcon from "@mui/icons-material/RiceBowl";

import RecipePreviewDialog from "./RecipePreviewDialog.jsx";

import defaultProfPic from "../images/remy.jpg";
import defaultRecipePic from "../images/recipe.jpg";

export default function RecipeCard({ recipe, origin }) {
  const token = localStorage.getItem("token");
  const navigate = useNavigate();

  const [numLikes, setNumLikes] = React.useState(0);
  const [isLiked, setIsLiked] = React.useState(false);
  const [rec, setRec] = React.useState(null);
  const [loading, setLoading] = React.useState(true);
  const [mealType, setMealType] = React.useState(null);
  const [inMealPlan, setInMealPlan] = React.useState(false);

  const [pictureIsHover, setPictureIsHover] = React.useState(false);
  const [cardIsHover, setCardIsHover] = React.useState(false);
  const [headerIsHover, setHeaderIsHover] = React.useState(false);
  const [titleIsHover, setTitleIsHover] = React.useState(false);

  const [open, setOpen] = React.useState(false);
  const [openLogin, setOpenLogin] = React.useState(false);
  const [openDeleteConf, setOpenDeleteConf] = React.useState(false);

  async function loadU() {
    const data = await fetchData(
      "GET",
      `api/recipe?recipeId=${recipe.id}`,
      {},
      token
    );
    return data;
  }

  React.useEffect(() => {
    async function loadRec() {
      const rec = await loadU();
      setRec(rec);
      if (token) {
        setIsLiked(rec.isLiked);
      }
      setNumLikes(rec.likes);
      setMealType(rec.mealType);
      setInMealPlan(rec.inMealPlan);
      setLoading(false);
    }
    loadRec();
  }, []);

  const navigateToAuthor = () => {
    navigate(`/profile/${rec.authorId}`);
  };

  const navigateToRecipe = () => {
    navigate(`/recipe/${rec.id}`);
    reloadPage();
  };

  const navigateToEdit = () => {
    navigate(`/editrecipe/${rec.id}`);
  };

  const handleLike = () => {
    if (token) {
      if (isLiked) {
        // unlike
        fetchData("POST", "api/unlike", { recipeId: recipe.id }, token);
        setNumLikes(parseInt(numLikes) - 1);
        setIsLiked(false);
      } else {
        // like
        fetchData("POST", "api/like", { recipeId: recipe.id }, token);
        setNumLikes(parseInt(numLikes) + 1);
        setIsLiked(true);
      }
    } else {
      setOpenLogin(true);
    }
  };

  const addToMealPlan = () => {
    if (token) {
      fetchData("POST", "api/meal_plan", { id: recipe.id }, token);
    } else {
      setOpenLogin(true);
    }
  };

  const removeFromMealPlan = () => {
    fetchData("DELETE", "api/meal_plan", { id: recipe.id }, token);
  };

  const navigateToMealSearch = () => {
    navigate(`/search/mealtypes=${mealType}`);
  };

  const reloadPage = () => {
    window.location.reload(false);
  };

  const deleteRecipe = () => {
    fetchData("DELETE", `api/recipe`, { recipeId: rec.id }, token);
    reloadPage();
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

  const likedStyle = { padding: "20px", color: "red" };
  const unlikedStyle = { padding: "20px", color: "black" };
  const cardActionStyle = { display: "flex", justifyContent: "space-between" };
  const editButton = { marginRight: "20px" };
  const mealPlanAction = { padding: "20px" };

  const cardHover = {
    transform: "scale3d(1.05, 1.05, 1)",
    transition: "transform 0.15s ease-in-out",
  };
  const cardNoHover = { transition: "transform 0.15s ease-in-out" };
  const recipePreviewButton = {
    position: "absolute",
    top: "80%",
    left: "50%",
    transform: "translate(-80px, -200px)",
    opacity: 1,
  };

  const headerHover = {
    cursor: "pointer",
    backgroundColor: "#FAFAFA",
    paddingRight: "40px",
    transform: "scale3d(1.05, 1.05, 1)",
    transition: "transform 0.15s ease-in-out",
  };
  const headerNoHover = {
    paddingRight: "40px",
    transition: "transform 0.15s ease-in-out",
  };

  const recipeTitleHover = {
    cursor: "pointer",
    transform: "scale3d(1.15, 1.15, 1)",
    transition: "transform 0.15s ease-in-out",
  };
  const recipeTitleNoHover = {
    cursor: "pointer",
    transition: "transform 0.15s ease-in-out",
  };

  const pictureHover = { opacity: 0.3, width: "350px", height: "194px" };
  const pictureNoHover = { width: "350px", height: "194px" };

  const mealTypeButton = { marginLeft: "10px" };

  const dialogActionStyle = { display: "flex", justifyContent: "flex-start" };
  const makeableStyle = {
    marginTop: "15px",
    color: "green",
    transform: "translate(10px, 0px)",
  };
  return (
    <>
      {loading ? (
        <Box sx={{ display: "flex" }}>
          <CircularProgress />
        </Box>
      ) : (
        <Card
          sx={{ maxWidth: 345 }}
          onMouseEnter={() => setCardIsHover(true)}
          onMouseLeave={() => setCardIsHover(false)}
          style={cardIsHover ? cardHover : cardNoHover}
        >
          <CardHeader
            onClick={navigateToAuthor}
            onMouseEnter={() => setHeaderIsHover(true)}
            onMouseLeave={() => setHeaderIsHover(false)}
            style={headerIsHover ? headerHover : headerNoHover}
            avatar={
              rec.authorPfp ? (
                <Avatar src={rec.authorPfp} />
              ) : (
                <Avatar src={defaultProfPic} />
              )
            }
            title={rec.authorName}
            subheader={rec.authorTitle ? rec.authorTitle : "Masterchef"}
            action={
              rec.isMakeable && (
                <Tooltip title="this recipe is makable using your pantry ingedients">
                  <DoneIcon style={makeableStyle} />
                </Tooltip>
              )
            }
          />
          <Box>
            {rec.photo ? (
              <CardMedia
                component="img"
                height="194"
                image={rec.photo}
                style={pictureIsHover ? pictureHover : pictureNoHover}
                onMouseEnter={() => setPictureIsHover(true)}
                onMouseLeave={() => setPictureIsHover(false)}
              />
            ) : (
              <CardMedia
                component="img"
                height="194"
                image={defaultRecipePic}
                onMouseEnter={() => setPictureIsHover(true)}
                onMouseLeave={() => setPictureIsHover(false)}
              />
            )}
          </Box>
          <CardContent>
            {pictureIsHover && (
              <Button
                variant="contained"
                style={recipePreviewButton}
                onMouseEnter={() => setPictureIsHover(true)}
                onMouseLeave={() => setPictureIsHover(false)}
                onClick={() => setOpen(true)}
              >
                See Recipe Preview
              </Button>
            )}
            <Typography
              variant="body1"
              aria-label="click to visit recipe detail"
              onClick={navigateToRecipe}
              onMouseEnter={() => setTitleIsHover(true)}
              onMouseLeave={() => setTitleIsHover(false)}
              style={titleIsHover ? recipeTitleHover : recipeTitleNoHover}
            >
              {rec.title}
            </Typography>
          </CardContent>
          <CardActions style={cardActionStyle}>
            <Tooltip title="Like">
              <IconButton aria-label="add to favorites">
                <FavoriteIcon
                  style={isLiked ? likedStyle : unlikedStyle}
                  onClick={handleLike}
                />
                <Typography>{numLikes}</Typography>
              </IconButton>
            </Tooltip>
            {origin !== "selfprofile" && (
              <Box>
                <Tooltip title="See All Recipes Of This Meal Type">
                  <Button
                    onClick={navigateToMealSearch}
                    style={mealTypeButton}
                    startIcon={computeIcon(mealType)}
                  >
                    {mealType}
                  </Button>
                </Tooltip>
              </Box>
            )}

            {inMealPlan ? (
              <Box>
                {origin === "mealplan" ? (
                  <Box>
                    <Tooltip title="Remove From Meal Plan">
                      <IconButton
                        style={mealPlanAction}
                        onClick={() => {
                          removeFromMealPlan();
                          reloadPage();
                          setInMealPlan(false);
                        }}
                      >
                        <MenuBookIcon />
                        <RemoveIcon />
                      </IconButton>
                    </Tooltip>
                  </Box>
                ) : (
                  <Box>
                    <Tooltip title="Remove From Meal Plan">
                      <IconButton
                        style={mealPlanAction}
                        onClick={() => {
                          removeFromMealPlan();
                          setInMealPlan(false);
                        }}
                      >
                        <MenuBookIcon />
                        <RemoveIcon />
                      </IconButton>
                    </Tooltip>
                  </Box>
                )}
              </Box>
            ) : (
              <Box>
                <Tooltip title="Add to Meal Plan">
                  <IconButton
                    style={mealPlanAction}
                    onClick={() => {
                      addToMealPlan();
                      setInMealPlan(true);
                    }}
                  >
                    <MenuBookIcon />
                    <AddIcon />
                  </IconButton>
                </Tooltip>
              </Box>
            )}

            {origin === "selfprofile" && (
              <Box>
                <Tooltip title="Edit">
                  <IconButton>
                    <EditIcon style={editButton} onClick={navigateToEdit} />
                  </IconButton>
                </Tooltip>

                <Tooltip title="Delete">
                  <IconButton>
                    <DeleteIcon
                      style={editButton}
                      onClick={() => setOpenDeleteConf(true)}
                    />
                  </IconButton>
                </Tooltip>
              </Box>
            )}
          </CardActions>

          <Dialog
            open={open}
            onClose={() => setOpen(false)}
            scroll={"paper"}
            aria-labelledby="recipe-detail-dialog"
            aria-describedby="recipe-detail-dialog"
            fullWidth
            maxWidth="sm"
          >
            <RecipePreviewDialog recipe={rec} />
            <DialogActions style={dialogActionStyle}>
              <Tooltip title="Like">
                <IconButton>
                  <FavoriteIcon
                    style={isLiked ? likedStyle : unlikedStyle}
                    onClick={handleLike}
                  />
                  <Typography>{numLikes}</Typography>
                </IconButton>
              </Tooltip>

              <Button
                endIcon={<MenuBookIcon />}
                variant="outlined"
                onClick={addToMealPlan}
              >
                Add To Meal Plan
              </Button>
              <Button
                variant="outlined"
                endIcon={<ArrowForwardIosIcon />}
                onClick={navigateToRecipe}
              >
                Go To Page
              </Button>
              <Button
                variant="outlined"
                endIcon={<CloseIcon />}
                onClick={() => setOpen(false)}
              >
                Close
              </Button>
            </DialogActions>
          </Dialog>

          <Dialog
            open={openLogin}
            onClose={() => setOpenLogin(false)}
            aria-labelledby="login-dialog"
            aria-describedby="login-dialog"
            fullWidth
            maxWidth="sm"
          >
            <DialogTitle>Uh Oh</DialogTitle>
            <DialogContent>
              <Typography>
                You must be a registered user to like and add recipes to your
                meal plan.
              </Typography>
            </DialogContent>
            <DialogActions>
              <Button onClick={() => navigate("/login")}>Login</Button>
              <Button onClick={() => navigate("/register")}>Register</Button>
            </DialogActions>
          </Dialog>

          <Dialog
            open={openDeleteConf}
            onClose={() => setOpenDeleteConf(false)}
            aria-labelledby="delete-recipe-confirmation-dialog"
            aria-describedby="delete-recipe-confirmation-dialog"
            fullWidth
            maxWidth="sm"
          >
            <DialogContent>
              <Typography>
                Are you sure you want to delete {rec.title}?
              </Typography>
            </DialogContent>
            <DialogActions>
              <Button variant="outlined" onClick={deleteRecipe}>
                Yes, Delete
              </Button>
              <Button
                variant="outlined"
                onClick={() => setOpenDeleteConf(false)}
              >
                No
              </Button>
            </DialogActions>
          </Dialog>
        </Card>
      )}
    </>
  );
}
