import React from "react";
import {
  Box,
  Typography,
  Divider,
  DialogTitle,
  DialogContent,
} from "@mui/material";

export default function RecipePreviewDialog({ recipe }) {
  const ingredStyle = {
    display: "flex",
    margin: "5px",
    textAlign: "center",
    justifyContent: "center",
  };
  const unitStyle = { marginRight: "5px" };
  const ingred = { marginRight: "10px" };

  const dividerStyle = { margin: "30px" };
  const flexBoxStyle = {
    display: "flex",
    justifyContent: "center",
    margin: "0px 0px",
  };
  const horiListSpacing = { marginLeft: "5px" };

  return (
    <>
      <DialogTitle>{recipe.title}</DialogTitle>
      <DialogContent>
        <Typography variant="body2">{recipe.description}</Typography>
        <Divider variant="middle" style={dividerStyle} />

        <Typography style={flexBoxStyle}>
          Meal Type: {recipe.mealType}
        </Typography>
        <Typography style={flexBoxStyle}>
          Cuisines:{" "}
          {recipe.cuisine
            .filter((_, index) => index !== recipe.cuisine.length - 1)
            .map((cuisine) => (
              <Typography style={horiListSpacing}>{cuisine}, </Typography>
            ))}
          {recipe.cuisine
            .filter((_, index) => index === recipe.cuisine.length - 1)
            .map((cuisine) => (
              <Typography style={horiListSpacing}>{cuisine} </Typography>
            ))}
        </Typography>
        {recipe.dietaries.length === 0 ? (
          <Typography></Typography>
        ) : (
          <Typography style={flexBoxStyle}>
            Dietaries:{" "}
            {recipe.dietaries
              .filter((_, index) => index !== recipe.dietaries.length - 1)
              .map((dietary, i) => (
                <Typography style={horiListSpacing}>{dietary},</Typography>
              ))}
            {recipe.dietaries
              .filter((_, index) => index === recipe.dietaries.length - 1)
              .map((dietary, i) => (
                <Typography style={horiListSpacing}>{dietary}</Typography>
              ))}
          </Typography>
        )}
        <Divider variant="middle" style={dividerStyle} />
        <Typography style={ingredStyle} variant="h6">
          Ingredients
        </Typography>
        <Typography style={ingredStyle}>Servings: {recipe.servings}</Typography>
        {recipe.ingredients.map((ingredient, i) => (
          <div style={ingredStyle}>
            <Typography style={unitStyle}>{ingredient.quantity}</Typography>
            <Typography style={ingred}>{ingredient.units}</Typography>
            <Typography>{ingredient.ingredient}</Typography>
          </div>
        ))}
        {recipe.utensils.length !== 0 && (
          <Box>
            <Divider variant="middle" style={dividerStyle} />
            <Typography style={ingredStyle} variant="h6">
              Utensils
            </Typography>
            {recipe.utensils.map((utensil, i) => (
              <Typography style={ingredStyle}>{utensil}</Typography>
            ))}
          </Box>
        )}
      </DialogContent>
    </>
  );
}
