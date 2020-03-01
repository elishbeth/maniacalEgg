import React, { Component } from "react";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import CheckBox from "@material-ui/core/Checkbox";
import NavBar from "./Components/NavBar";
import "./App.css";

class App extends Component {
  render() {
    return (
      <div className="App">
        <div>
          <NavBar />
        </div>
        <div className = "Checkboxes">
          <FormControlLabel
            control={<CheckBox label="yooooo">yoooo</CheckBox>}
            label="yooooo"
          />
        </div>
      </div>
    );
  }
}

export default App;
