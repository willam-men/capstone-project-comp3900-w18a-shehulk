CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- create users table
CREATE TABLE IF NOT EXISTS users (
    "id" serial UNIQUE,
    "username" text NOT NULL UNIQUE,
    "name" text NOT NULL,
    "email" text NOT NULL UNIQUE,
    "password" text NOT NULL,
    "followerIds" int[] NOT NULL,
    "followingIds" int[] NOT NULL,
    "profilePic" text,
    "publishedRecipes" uuid[] NOT NULL,
    "savedRecipes" uuid[] NOT NULL,
    "bio" text,
    "title" text,
    "pantry" text[] DEFAULT array[]::text[],
    "mealPlans" uuid[] NOT NULL DEFAULT array[]::uuid[],
    PRIMARY KEY(id)
);

-- Store user sessions 
CREATE TABLE IF NOT EXISTS tokens (
    "jsonWebToken" text UNIQUE NOT NULL,
    "userId" int NOT NULL, 
    PRIMARY KEY ("jsonWebToken"),
    FOREIGN KEY("userId") references users(id)
);

-- create recipes table
CREATE TABLE IF NOT EXISTS recipes(
    "id" uuid DEFAULT uuid_generate_v4() NOT NULL,
    "status" text NOT NULL DEFAULT 'Published',
    "title" text NOT NULL,
    "description" text,
    "authorName" text NOT NULL,
    "authorId" int NOT NULL,
    "authorPfp" text,
    "servings" int NOT NULL,
    "ingredients" jsonb NOT NULL,
    "method" text[] NOT NULL,
    "mealType" text NOT NULL,
    "photo" text DEFAULT NULL,
    "viewCount" int NOT NULL DEFAULT 0,
    "likedList" int[] NOT NULL DEFAULT array[]::int[],
    "savedList" int[] NOT NULL DEFAULT array[]::int[], -- might not need to store this info
    "lastUpdated" timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "utensils" text[] NOT NULL,
    "dietaries" text[] NOT NULL,
    "difficulty" text,
    "cuisine" text[] NOT NULL,
    "prepTime" text NOT NULL,
    "cookTime" text NOT NULL,
    PRIMARY KEY(id)
);

-- create comments table
CREATE TABLE IF NOT EXISTS comments (
    "id" uuid DEFAULT uuid_generate_v1() NOT NULL,
    "recipeId" uuid NOT NULL,
    "userId" int NOT NULL,
    "username" text NOT NULL,
    "profilePic" text,
    "comment" text,
    "photo" text,
    "rating" float,
    PRIMARY KEY(id),
    FOREIGN KEY("recipeId") references recipes(id),
    FOREIGN KEY("userId") references users(id)
);

CREATE TABLE IF NOT EXISTS ingredients (
    "ingredient" text UNIQUE,
    "recipes" uuid[] NOT NULL DEFAULT array[]::uuid[],
    PRIMARY KEY ("ingredient")
);