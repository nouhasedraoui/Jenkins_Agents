module tn.git.demo {
    requires javafx.controls;
    requires javafx.fxml;


    opens tn.git.demo to javafx.fxml;
    exports tn.git.demo;
}