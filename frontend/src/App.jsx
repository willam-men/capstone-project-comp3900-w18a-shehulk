import React from "react";
import "./App.css";

import Home from "./pages/Home";
import Explore from "./pages/Explore";
import Login from "./pages/Login";
import Register from "./pages/Register";
import RecipeDetail from "./pages/RecipeDetail";
import Feed from "./pages/Feed";
import RecipeCreate from "./pages/RecipeCreate";
import LoginWelcome from "./pages/LoginWelcome";
import NotFound from "./pages/NotFound";
import Profile from "./pages/Profile";
import RecipeEdit from "./pages/RecipeEdit";
import PersonalSettings from "./pages/PersonalSettings";
import Search from "./pages/Search";
import SearchResults from "./pages/SearchResults";
import AllUsers from "./pages/AllUsers";
import MealPlan from "./pages/MealPlan";
import ShoppingList from "./pages/ShoppingList";
import Pantry from "./pages/Pantry";
import MakeableRecipes from "./pages/MakeableRecipes";

import NavBar from "./components/NavBar";
import AuthNavBar from "./components/AuthNavBar";

import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  const [isLoggedIn, setIsLoggedIn] = React.useState(false);
  const [userProfPic, setUserProfPic] = React.useState(null);

  // upon render check if there is a token stored in local storage
  // if token then the user is logged, forgot to log out last time in with valid token
  // if nothing is found the user is not logged in
  React.useEffect(() => {
    const currToken = localStorage.getItem("token");
    if (currToken) {
      setIsLoggedIn(true);
    }
  }, []);

  return (
    <div className="App">
      <BrowserRouter>
        {isLoggedIn && (
          <NavBar
            setUserProfPic={setUserProfPic}
            userProfPic={userProfPic}
            setIsLoggedIn={setIsLoggedIn}
          />
        )}
        {!isLoggedIn && <AuthNavBar />}
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/explore" element={<Explore />} />
          <Route
            path="/login"
            element={<Login setIsLoggedIn={setIsLoggedIn} />}
          />
          <Route
            path="/register"
            element={<Register setIsLoggedIn={setIsLoggedIn} />}
          />
          <Route path="/recipe/:recipeid" element={<RecipeDetail />} />
          <Route path="/feed" element={<Feed />} />
          <Route path="/createrecipe" element={<RecipeCreate />} />
          <Route path="/editrecipe/:recipeid" element={<RecipeEdit />} />
          <Route path="/loginwelcome" element={<LoginWelcome />} />
          <Route path="/notfound" element={<NotFound />} />
          <Route
            path="/profile/:userid"
            element={<Profile setUserProfPic={setUserProfPic} />}
          />
          <Route path="/personalsettings" element={<PersonalSettings />} />
          <Route path="/search" element={<Search />} />
          <Route path="/search/:terms" element={<SearchResults />} />
          <Route path="/users" element={<AllUsers />} />
          <Route path="/mealplan" element={<MealPlan />} />
          <Route path="/shoppinglist" element={<ShoppingList />} />
          <Route path="/pantry" element={<Pantry />} />
          <Route path="/makeable" element={<MakeableRecipes />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
