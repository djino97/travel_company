myApp.controller('dialogShow', function ($scope, $mdDialog, $sessionStorage) {

    $scope.openFromLeft = function () {
        setTimeout(function () {
            $scope.$apply(function () {
                if (!$sessionStorage.isOpenDialog) {
                    $scope.setParametersDialog = setParametersDialog($scope, $mdDialog);
                    $sessionStorage.isOpenDialog = true;
                }
            })
        }, 2000);
    };

    $scope.openFromLeft();
});

function setParametersDialog($scope, $mdDialog) {
    $mdDialog.show({
            locals: {
                descriptionDialog: $scope.descriptionDialog,
            },
            template: getTemplate(),
            clickOutsideToClose: false,
            openFrom: {
                top: -50,
                width: 1300,
                height: 20
            },
            closeTo: {
                top: -50,
                width: 1300,
                height: 20
            },
            controller: closeDialog_,
        }
    );

}

function getTemplate() {

    let template = '<md-dialog  aria-label="List dialog">' +
        '<md-dialog-content class="md_dialog_content_border">' +
        '{{descriptionDialog[0].border}}' +
        '</md-dialog-content>' +
        '<md-dialog-content class="md_dialog_content">' +
        '<div style="display: flex;">' +
        '<div style="width: 285px; height: 200px;">' +
        '<img class="img_dialog" src="{{descriptionDialog[0].uriImage}}">' +
        '</div>' +
        '<div>' +
        '<div>{{descriptionDialog[0].greeting}}</div>' +
        '</br> <div>{{descriptionDialog[0].description}}</div>' +
        '</div>' +
        '</div>' +
        '</md-dialog-content>' +

        '<md-dialog-actions>' +
        '<md-button ng-click="closeDialog()" class="md-primary">' +
        'Понятно' +
        '</md-button>' +
        '</md-dialog-actions>' +
        '</md-dialog>';

    return template;
}

function closeDialog_($scope, $mdDialog) {
    $scope.descriptionDialog = getDescription();
    $scope.closeDialog = function () {
        $mdDialog.hide();
    }
}

function getDescription() {
    return [{
        border: 'Действующие акции и скидки',
        greeting: 'Путешественник, добро пожаловать на сайт бронирования туров!',
        description: 'Акции от отелей, туроператоров и туристических партнеров - дают возможность купить ' +
            'Вам туры по самым выгодным ценам. Торопитесь! Время акций и количество предложений с подарками и ' +
            'скидками всегда ограничено.',
        uriImage: 'static/css/image_templates/sales.png'
    }];
}