import React from "react";
import {
  Box,
  Button,
  TextField,
  FormControl,
  Select,
  IconButton,
  MenuItem,
  Typography,
  FormHelperText,
  Autocomplete,
  CircularProgress,
} from "@mui/material";
import DeleteIcon from "@mui/icons-material/Delete";
import NoFoodIcon from "@mui/icons-material/NoFood";
import fetchData from "../helper.js";

export default function RecipeAddIngredients({
  formData,
  setFormData,
  validateData,
}) {
  const defaultAmountErrorMsg =
    "Please type a number and/or fraction (e.g. 1 1/2, 2 or 1/4)";
  const defaultUnitErrorMsg =
    "Please select a unit. If there is no unit, select 'None'";
  const defaultIngredientErrorMsg =
    "Ingredients are validated against our database. If there are no matches, please select a similar ingredient.";

  const [amount, setAmount] = React.useState(null);
  const [units, setUnits] = React.useState("None");
  const [ingredient, setIngredient] = React.useState("");
  const [ingredientsOptions, setIngredientsOptions] = React.useState([]);
  const [reset, setReset] = React.useState(true);

  const [amountError, setAmountError] = React.useState(false);
  const [ingredientError, setIngredientError] = React.useState(false);
  const [ingredientErrorMsg, setIngredientErrorMsg] = React.useState(
    defaultIngredientErrorMsg
  );
  const [overallError, setOverallError] = React.useState(false);

  const unitOptions = [
    "cup",
    "g",
    "ml",
    "tsp",
    "tbsp",
    "bag",
    "bulb",
    "bunch",
    "bundle",
    "clove",
    "head",
    "kg",
    "loaf",
    "m",
    "scoop",
    "stalk",
    "None",
  ];

  async function loadIngredients() {
    const data = await fetchData("GET", `api/ingredients`, {});
    return data;
  }

  React.useEffect(() => {
    async function loadIngredient() {
      setIngredientsOptions(await loadIngredients());
    }
    loadIngredient();
  }, []);

  const reformatIngredientList = () => {
    let reformattedIngredientList = [];
    for (let i = 0; i < formData.ingredients.length; i++) {
      let ingredient = formData.ingredients[i];

      let ingredientFormatted = "";
      if (ingredient.quantity) {
        ingredientFormatted += ingredient.quantity + " ";
      }
      if (ingredient.units) {
        ingredientFormatted += ingredient.units + " ";
      }
      ingredientFormatted += ingredient.ingredient + " ";
      reformattedIngredientList.push(ingredientFormatted);
    }
    return reformattedIngredientList;
  };

  const [formattedIngredientList, setIngredientsFormatted] = React.useState(
    () => reformatIngredientList()
  );

  React.useEffect(() => {
    if (validateData === true) {
      if (formData.ingredients.length === 0) {
        setOverallError(true);
      } else {
        setOverallError(false);
      }
    }
  }, [validateData, formData.ingredients.length]);

  const checkFraction = (frac) => {
    const fraction = frac.trim().split("/");
    if (fraction.length !== 2 || isNaN(fraction[0]) || isNaN(fraction[1])) {
      setAmountError(true);
      return false;
    }
    return true;
  };

  const validateAmount = () => {
    if (amount == 0) {
      setAmountError(true);
      return false;
    }
    if (!amount) {
      if (units !== "None") {
        setAmountError(true);
        return false;
      } else {
        setAmountError(false);
        return true;
      }
    }
    const amountList = amount.trim().split(/\s+/);
    if (amountList.length > 2) {
      setAmountError(true);
      return false;
    }
    if (amountList.length === 2 && isNaN(amountList[0])) {
      // check second is a fraction
      if (!checkFraction(amountList[1])) {
        return false;
      }
    }
    if (amountList.length === 1 && isNaN(amountList[0])) {
      if (!checkFraction(amountList[0])) {
        return false;
      }
    }
    setAmountError(false);
    return true;
  };

  const validateIngredients = () => {
    if (!ingredient) {
      setIngredientError(true);
      setIngredientErrorMsg(
        "Please enter an ingredient. If there are no matches, please select a similar ingredient."
      );
      return false;
    } else {
      // check whether formData.ingredients contains ingredient already
      for (let index in formData.ingredients) {
        if (formData.ingredients[index].ingredient === ingredient) {
          setIngredientError(true);
          setIngredientErrorMsg(
            "This ingredient has already been added into the ingredients list. Please add a new ingredient"
          );
          return false;
        }
      }
      setIngredientError(false);
      setIngredientErrorMsg(defaultIngredientErrorMsg);
      return true;
    }
  };

  const addIngredient = () => {
    // need to check for valid inputs first
    console.log(validateAmount())
    if (validateAmount() && validateIngredients()) {
      // then add ingredient to list
      let listIngredients = formData.ingredients;
      let dicIngredients = { quantity: "", units: "", ingredient: ingredient };
      if (amount) {
        dicIngredients.quantity = amount;
      }
      if (units !== "None") {
        dicIngredients.units = units;
      }
      listIngredients.push(dicIngredients);
      setFormData({
        ...formData,
        ingredients: listIngredients,
      });
      setIngredient("");
      setAmount("");
      setUnits("None");
      setIngredientsFormatted(reformatIngredientList());
      setReset(!reset);
      if (overallError) {
        setOverallError(false);
      }
    }
  };

  const deleteRow = (index) => {
    let listIngredients = formData.ingredients;
    listIngredients.splice(index, 1);
    setFormData({
      ...formData,
      ingredients: listIngredients,
    });
    setIngredientsFormatted(reformatIngredientList());
  };

  const divStyle = {
    display: "grid",
    alignItems: "start",
    marginBottom: "30px",
  };
  // const selectStyle = { marginBottom: '30px', width: '20%', float: "left" }
  const labelStyle = { textAlign: "left" };
  const label2Style = { textAlign: "left", paddingBottom: "20px" };
  const gridStyle = {
    display: "grid",
    alignItems: "center",
    gridTemplateColumns: "30% 20% 50%",
  };
  // const flexStyle = {display: 'flex', alignItems: 'center'}
  const submitButtonStyle = {
    marginLeft: "auto",
    width: "150px",
    minHeight: "50px",
    display: "flex",
    flexDirection: "row",
  };
  const textStyle = { minWidth: "25%", marginRight: "30px", textAlign: "left" };
  const iconStyle = { float: "right" };
  const helperText = {
    textAlign: "left",
    letterSpacing: "0.03333em",
    fontFamily: "Arial",
    color: "#d4323e",
    fontSize: "0.75rem",
  };

  return (
    <>
      {ingredientsOptions.length === 0 ? (
        <Box sx={{ display: "flex" }}>
          <CircularProgress />
        </Box>
      ) : (
        <div>
          <div style={divStyle}>
            <Typography variant="h5" style={labelStyle}>
              Add Ingredients
            </Typography>

            <div style={gridStyle}>
              <div style={divStyle}>
                <Typography variant="h6" style={labelStyle}>
                  Amount{" "}
                </Typography>
                <TextField
                  style={textStyle}
                  value={amount}
                  onChange={(e) => {
                    setAmount(e.target.value);
                  }}
                  error={amountError}
                  helperText={defaultAmountErrorMsg}
                />
              </div>

              <div style={divStyle}>
                <Typography variant="h6" style={labelStyle}>
                  Units{" "}
                </Typography>
                <Select
                  labelId="units-select-label"
                  id="units-select"
                  value={units}
                  label="units"
                  style={textStyle}
                  onChange={(e) => {
                    setUnits(e.target.value);
                  }}
                >
                  {unitOptions.map((unit) => (
                    <MenuItem value={unit}>{unit}</MenuItem>
                  ))}
                </Select>
                <FormHelperText>{defaultUnitErrorMsg}</FormHelperText>
              </div>

              <div style={divStyle}>
                <Typography variant="h6" style={label2Style}>
                  Ingredient{" "}
                </Typography>
                <Autocomplete
                  key={reset}
                  id="tags-standard"
                  options={ingredientsOptions}
                  getOptionLabel={(option) => option.ingredient}
                  sx={{ minHeight: "30px" }}
                  onChange={(e, v) => {
                    setIngredient(v.ingredient);
                  }}
                  renderInput={(params) => (
                    <TextField
                      {...params}
                      variant="standard"
                      helperText={ingredientErrorMsg}
                      error={ingredientError}
                    />
                  )}
                />
              </div>
            </div>

            <Button
              variant="contained"
              aria-label="register-button"
              id="submit-recipe"
              style={submitButtonStyle}
              onClick={() => addIngredient()}
            >
              Add Ingredient
            </Button>
          </div>

          <div style={divStyle}>
            <FormControl>
              <Typography variant="h5" style={labelStyle}>
                Ingredient List
              </Typography>
              <Typography style={helperText}>
                {overallError ? "Please add at least one ingredient" : ""}
              </Typography>
              <Box style={divStyle}>
                {formattedIngredientList.map((option, index) => (
                  <div key={index}>
                    <Box>
                      <IconButton
                        sx={iconStyle}
                        aria-label="delete"
                        onClick={() => deleteRow(index)}
                      >
                        <DeleteIcon />
                      </IconButton>
                    </Box>
                    <Box sx={{ textAlign: "left" }}>{option}</Box>
                  </div>
                ))}
                <br />

                {formData.ingredients.length === 0 ? (
                  <NoFoodIcon style={{ margin: "auto" }} />
                ) : (
                  ""
                )}
                {formData.ingredients.length === 0
                  ? "No Ingredients have been added"
                  : ""}
              </Box>
            </FormControl>
          </div>
        </div>
      )}
    </>
  );
}
