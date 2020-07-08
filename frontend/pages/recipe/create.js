import Head from "next/head";
import { withRouter } from "next/router";
import React from "react";

import RecipeAPI from "../../lib/api/recipe";
import Error from "../../components/Error/Error";

class CreateRecipe extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: false,
      recipe: {
        name: "",
        method: "",
        cook_time: "",
        author: "",
        diet_req: [],
        ingredients: [],
        meal_cat: [],
      },
      error: null,
    };
  }

  componentDidMount() {}

  handleSubmit = async (e) => {
    this.setState({ loading: true });
    RecipeAPI.create(this.state.recipe, "")
      .then((res) => {
        console.log(res);
        if (res.status == 201) {
          this.props.router.push("/recipe/" + res.data.id);
        }
        this.setState({ loading: false });
      })
      .catch((err) => {
        this.setState({ loading: false });
        console.log("skrt", err.response);
      }); // TODO: map the errors to fields
  };

  handleInputChange = ({ target }, name) => {
    this.setState((prev) => ({
      ...prev,
      recipe: { ...prev.recipe, [name]: target.value },
    }));
  };

  render() {
    if (this.state.error) {
      return <Error message={this.state.error.statusText} />;
    }

    if (this.state.loading) {
      return <p>Loading</p>;
    }
    return (
      <>
        <Head>
          <title>Pantry Pirate | Create</title>
        </Head>
        <div className="container">
          <div className="columns is-centered">
            <div className="box column is-10">
              <h1 className="title">New Recipe</h1>
              <form>
                <div className="field">
                  <label className="label">Title</label>
                  <input
                    className="input"
                    placeholder="Title"
                    value={this.state.recipe.name}
                    onChange={(e) => this.handleInputChange(e, "name")}
                  />
                </div>
                <div className="field">
                  <label className="label">Author ID (for the demo)</label>
                  <input
                    className="input"
                    placeholder="Author Id"
                    value={this.state.recipe.author}
                    onChange={(e) => this.handleInputChange(e, "author")}
                  />
                </div>
                <div className="field">
                  <label className="label">Cook Time</label>
                  <input
                    className="input"
                    placeholder="Cook Time"
                    value={this.state.recipe.cook_time}
                    onChange={(e) => this.handleInputChange(e, "cook_time")}
                  />
                </div>
                <div className="field">
                  <label className="label">Method</label>
                  <textarea
                    className="textarea"
                    placeholder="Method"
                    value={this.state.recipe.method}
                    onChange={(e) => this.handleInputChange(e, "method")}
                  ></textarea>
                </div>
              </form>
              <br />

              <div className="buttons">
                <button
                  className={`button is-light is-success ${
                    this.state.loading ? "is-loading" : null
                  }`}
                  onClick={this.handleSubmit}
                >
                  Add Recipe
                </button>
              </div>
            </div>
          </div>
        </div>
      </>
    );
  }
}

// You can't use hooks (i.e. useRouter) with a class component in react
export default withRouter(CreateRecipe);
