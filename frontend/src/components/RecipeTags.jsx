import React from "react";
import {
  Box,
  Button,
  Checkbox,
  FormControl,
  Typography,
  FormControlLabel,
} from "@mui/material";
import SoupKitchenIcon from "@mui/icons-material/SoupKitchen";
import CoffeeIcon from "@mui/icons-material/Coffee";
import CakeIcon from "@mui/icons-material/Cake";
import CookieIcon from "@mui/icons-material/Cookie";
import BreakfastDiningIcon from "@mui/icons-material/BreakfastDining";
import DinnerDiningIcon from "@mui/icons-material/DinnerDining";
import RiceBowlIcon from "@mui/icons-material/RiceBowl";
import {
  cuisineOptions,
  dietaryOptions,
  mealTypeOptions,
} from "../RecipeTypes";

export default function RecipeTags({ formData, setFormData, validateData }) {
  const [mealTypeError, setMealTypeError] = React.useState(false);
  const [cuisineError, setCuisineError] = React.useState(false);

  React.useEffect(() => {
    if (validateData === true) {
      if (!formData.mealType) {
        setMealTypeError(true);
      }
      if (formData.cuisines.length === 0) {
        setCuisineError(true);
      }
    }
  }, [validateData, formData]);

  const checkCuisines = () => {
    let array = new Array(cuisineOptions.length).fill(false);
    cuisineOptions.map((value, index) => {
      if (formData.cuisines.includes(value)) {
        array[index] = true;
      }
    });
    return array;
  };

  const checkDietaries = () => {
    let array = new Array(dietaryOptions.length).fill(false);
    dietaryOptions.map((value, index) => {
      if (formData.dietaries.includes(value)) {
        array[index] = true;
      }
    });
    return array;
  };

  const [checkedStateCuisines, setCheckedStateCuisines] = React.useState(
    checkCuisines()
  );
  const [checkedStateDietaries, setCheckedStateDietaries] = React.useState(
    checkDietaries()
  );

  const handleMealType = (mealType) => {
    setFormData({
      ...formData,
      mealType: mealType,
    });
    if (mealTypeError) {
      setMealTypeError(false);
    }
  };

  const handleOnChangeCuisine = (position) => {
    const updatedCheckedState = checkedStateCuisines.map((item, index) =>
      index === position ? !item : item
    );

    setCheckedStateCuisines(updatedCheckedState);
    const selectedCuisines = formData.cuisines;

    for (let index in updatedCheckedState) {
      const currentState = updatedCheckedState[index];
      if (currentState && !selectedCuisines.includes(cuisineOptions[index])) {
        selectedCuisines.push(cuisineOptions[index]);
        if (cuisineError) {
          setCuisineError(false);
        }
      }
      if (!currentState && selectedCuisines.includes(cuisineOptions[index])) {
        selectedCuisines.splice(cuisineOptions[index]);
      }
    }

    setFormData({
      ...formData,
      cuisines: selectedCuisines,
    });
  };

  const handleOnChangeDietaries = (position) => {
    const updatedCheckedState = checkedStateDietaries.map((item, index) =>
      index === position ? !item : item
    );

    setCheckedStateDietaries(updatedCheckedState);
    const dietaries = formData.dietaries;

    for (let index = 0; index < updatedCheckedState.length; index++) {
      const currentState = updatedCheckedState[index];
      if (currentState && !dietaries.includes(dietaryOptions[index])) {
        dietaries.push(dietaryOptions[index]);
      }
      if (!currentState && dietaries.includes(dietaryOptions[index])) {
        dietaries.splice(dietaryOptions[index]);
      }
    }
    setFormData({
      ...formData,
      dietaries: dietaries,
    });
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

  const divStyle = {
    display: "grid",
    alignItems: "start",
    marginBottom: "30px",
  };
  const selectStyle = { marginBottom: "30px", float: "left" };
  const labelStyle = { textAlign: "left" };
  const basicFlexStyle = { display: "flex", minWidth: "300px" };
  const flexStyle = {
    display: "flex",
    flexDirection: "row",
    justfyContent: "flexStart",
    flexWrap: "wrap",
    alignContent: "spaceAround",
  };
  const checkboxStyle = {
    display: "flex",
    flexDirection: "column",
    width: "200px",
    paddingRight: "20%",
  };
  const helperText = {
    textAlign: "left",
    letterSpacing: "0.03333em",
    fontFamily: "Arial",
    color: "#d4323e",
    fontSize: "0.75rem",
  };

  return (
    <>
      <div style={divStyle}>
        <FormControl required style={selectStyle}>
          <Typography
            variant="h5"
            style={{ textAlign: "left", marginBottom: "10px" }}
          >
            Tags
          </Typography>
          <Typography variant="h6" style={labelStyle}>
            Meal Type
          </Typography>
          <div style={flexStyle}>
            {mealTypeOptions.map((mealType) => (
              <Button
                variant={
                  formData.mealType === mealType ? "contained" : "outlined"
                }
                startIcon={computeIcon(mealType)}
                style={{
                  marginRight: "30px",
                  width: "130px",
                  height: "50px",
                  marginBottom: "10px",
                }}
                onClick={() => {
                  handleMealType(mealType);
                }}
                key={mealType}
              >
                {mealType}
              </Button>
            ))}
          </div>
          <Typography style={helperText}>
            {mealTypeError ? "Please select a meal type" : ""}
          </Typography>
        </FormControl>

        <FormControl required style={selectStyle}>
          <Typography variant="h6" style={labelStyle}>
            Cuisine
          </Typography>
          <Typography style={helperText}>
            {cuisineError ? "Please select at least one cuisine" : ""}
          </Typography>
          <Box style={basicFlexStyle}>
            <Box sx={checkboxStyle}>
              {cuisineOptions
                .filter((_, index) => index % 2 === 0)
                .map((cuisine, index) => (
                  <FormControlLabel
                    control={
                      <Checkbox
                        checked={checkedStateCuisines[2 * index]}
                        onChange={() => handleOnChangeCuisine(2 * index)}
                      />
                    }
                    label={cuisine}
                  />
                ))}
            </Box>
            <Box sx={checkboxStyle}>
              {cuisineOptions
                .filter((_, index) => index % 2 !== 0)
                .map((cuisine, index) => (
                  <FormControlLabel
                    control={
                      <Checkbox
                        checked={checkedStateCuisines[2 * index + 1]}
                        onChange={() => handleOnChangeCuisine(2 * index + 1)}
                      />
                    }
                    label={cuisine}
                  />
                ))}
            </Box>
          </Box>
        </FormControl>

        <FormControl required style={selectStyle}>
          <Typography variant="h6" style={labelStyle}>
            Dietaries
          </Typography>
          <Box style={basicFlexStyle}>
            <Box sx={checkboxStyle}>
              {dietaryOptions
                .filter((_, index) => index % 2 === 0)
                .map((cuisine, index) => (
                  <FormControlLabel
                    control={
                      <Checkbox
                        checked={checkedStateDietaries[2 * index]}
                        onChange={() => handleOnChangeDietaries(2 * index)}
                      />
                    }
                    label={cuisine}
                  />
                ))}
            </Box>
            <Box sx={checkboxStyle}>
              {dietaryOptions
                .filter((_, index) => index % 2 !== 0)
                .map((cuisine, index) => (
                  <FormControlLabel
                    control={
                      <Checkbox
                        checked={checkedStateDietaries[2 * index + 1]}
                        onChange={() => handleOnChangeDietaries(2 * index + 1)}
                      />
                    }
                    label={cuisine}
                  />
                ))}
            </Box>
          </Box>
        </FormControl>
      </div>
    </>
  );
}
