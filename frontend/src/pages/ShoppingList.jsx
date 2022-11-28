import React from "react";
import fetchData from "../helper.js";
import { useNavigate } from "react-router-dom";

import { Paper, Divider, Typography, Box, Button } from "@mui/material";

export default function ShoppingList() {
  const token = localStorage.getItem("token");
  const navigate = useNavigate();

  const [shoppingList, setShoppingList] = React.useState([]);
  const [inCart, setInCart] = React.useState([]);

  // fetch ingredients to buy
  async function loadShoppingList() {
    const data = await fetchData(
      "GET",
      "api/missing_ingredients",
      { token: token },
      token
    );
    return data.ingredients;
  }

  // on load this calls the above function and fetches the recipes
  React.useEffect(() => {
    async function loadLists() {
      const shoppingOutput = await loadShoppingList();
      setShoppingList(shoppingOutput);
      setInCart(new Array(shoppingOutput.length).fill(false));
    }
    loadLists();
  }, []);

  const handleRemoveIngredientPantry = (index, ingredient) => {
    fetchData("POST", "api/pantry", { add: [], delete: [ingredient] }, token);
    // remove update the incart array
    const newCart = [...inCart];
    newCart.splice(index, 1, false);
    setInCart(newCart);
  };

  const handleAddIngredientToPantry = (index, ingredient) => {
    fetchData("POST", "api/pantry", { add: [ingredient], delete: [] }, token);
    // remove update the incart array
    const newCart = [...inCart];
    newCart.splice(index, 1, true);
    setInCart(newCart);
  };

  const paperStyle = {
    padding: "100px",
    width: "70vw",
    margin: "50px auto",
    alignItems: "center",
  };
  const listStyle = { width: "400px", margin: "50px auto" };
  const ingredStyle = {
    display: "flex",
    justifyContent: "space-between",
    margins: "10px 5px",
    marginRight: "10px",
  };
  const ingredText = { marginTop: "5px" };
  const ingredAddedText = { marginTop: "5px", textDecoration: "line-through" };

  return (
    <>
      <Paper style={paperStyle}>
        <Typography variant="h4">Shopping List</Typography>
        <Box style={listStyle}>
          {shoppingList.map((ingredient, index) => (
            <Box>
              {inCart[index] ? (
                <Box style={ingredStyle}>
                  <Typography style={ingredAddedText}>{ingredient}</Typography>
                  <Button
                    onClick={() => {
                      handleRemoveIngredientPantry(index, ingredient);
                    }}
                  >
                    Remove From Cart
                  </Button>
                </Box>
              ) : (
                <Box style={ingredStyle}>
                  <Typography style={ingredText}>{ingredient}</Typography>
                  <Button
                    onClick={() => {
                      handleAddIngredientToPantry(index, ingredient);
                    }}
                  >
                    Add To Cart
                  </Button>
                </Box>
              )}
              <Divider light />
            </Box>
          ))}
        </Box>
        <Button onClick={() => navigate("/pantry")} variant="contained">
          Go To Pantry List
        </Button>
      </Paper>
    </>
  );
}
