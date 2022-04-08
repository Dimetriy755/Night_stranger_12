<?php

$data = explode("\n", file_get_contents('lead.log'));
$data = array_filter(array_reverse($data));

$titles = [];
$leads = [];
foreach ($data as $value) {
    $row = json_decode($value, true);
    $titles = array_merge($titles, array_keys($row));
    $leads[] = $row;
}

$titles = array_unique($titles);
$titles = array_diff($titles, ['date', 'url']);

?>
<html>
<head>
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
</head>
<body>
<table class="table table-striped">
    <thead>
    <tr>
        <th>Date</th>
        <th>Url</th>
        <?php foreach ($titles as $title): ?>
            <th><?= ucfirst(strtolower($title)); ?></th>
        <?php endforeach; ?>
    </tr>
    </thead>
    <tbody>
    <?php foreach ($leads as $lead): ?>
        <tr>
            <td><?= $lead['date'] ?? ''; ?></td>
            <td><?= urldecode($lead['url'] ?? ''); ?></td>
            <?php foreach ($titles as $title): ?>
                <td><?= $lead[$title] ?? ''; ?></td>
            <?php endforeach; ?>
        </tr>
    <?php endforeach; ?>
    </tbody>
</table>
</body>
</html>

